from __future__ import unicode_literals

from django.conf import settings
from django.contrib import auth
from django import test as django_test

import volatildap


# Helpers
# =======


class LdapBasedTestCase(django_test.TestCase):
    @classmethod
    def setUpClass(cls):
        super(LdapBasedTestCase, cls).setUpClass()
        cls.ldap_server = volatildap.LdapServer(
            schemas=['core.schema', 'cosine.schema', 'nis.schema', 'inetorgperson.schema'],
            initial_data={
                'ou=people': {
                    'objectClass': [b'organizationalUnit'],
                    'ou': [b'People'],
                },
                'ou=groups': {
                    'objectClass': [b'organizationalUnit'],
                    'ou': [b'Groups'],
                },
            },
        )

    @classmethod
    def tearDownClass(cls):
        cls.ldap_server.stop()
        super(LdapBasedTestCase, cls).tearDownClass()

    def setUp(self):
        super(LdapBasedTestCase, self).setUp()
        self.ldap_server.start()
        settings.PAPAYA_LDAP_SERVER_URI = self.ldap_server.uri


# Tests
# =====


class AuthTest(LdapBasedTestCase):
    def test_login(self):
        self.ldap_server.add({
            'uid=jdoe,ou=people': {
                'objectClass': [b'inetOrgPerson'],
                'sn': [b'Doe'],
                'givenName': [b'John'],
                'cn': [b'John Doe'],
                'uid': [b'jdoe'],
                'mail': [b'john.doe@example.org'],
                'userPassword': [b'{SSHA}5N08LOuGYl8uDLlUa1QJJboh9swe/uH2'],
            },
            'cn=admins,ou=groups': {
                'objectClass': [b'posixGroup'],
                'cn': [b'admins'],
                'gidNumber': [b'42'],
                'memberUid': [b'jdoe'],
            },
        })

        user = auth.authenticate(username='jdoe', password='mypass')
        self.assertIsNotNone(user)
        self.assertEqual("John", user.first_name)
        self.assertEqual("Doe", user.last_name)
        self.assertEqual('john.doe@example.org', user.email)
        self.assertEqual(1, user.groups.count())
        self.assertEqual('admins', user.groups.get().name)

    def test_login_failure(self):
        self.ldap_server.add({
            'uid=jdoe,ou=people': {
                'objectClass': [b'inetOrgPerson'],
                'sn': [b'Doe'],
                'givenName': [b'John'],
                'cn': [b'John Doe'],
                'uid': [b'jdoe'],
                'mail': [b'john.doe@example.org'],
                'userPassword': [b'{SSHA}5N08LOuGYl8uDLlUa1QJJboh9swe/uH2'],
            },
        })

        user = auth.authenticate(username='jdoe', password='badpass')
        self.assertIsNone(user)

        user = auth.authenticate(username='john.doe@example.org', password='badpass')
        self.assertIsNone(user)
