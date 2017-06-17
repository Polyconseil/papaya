from __future__ import unicode_literals

import ldap
import ldap.filter

from papaya.conf import settings
from django.contrib.auth.models import User, Group


class LdapBackend:
    """
    Authenticate against LDAP.
    """

    @classmethod
    def prepare_query(cls, query, queryargs):
        return ldap.filter.filter_format(query, queryargs)

    def authenticate(self, username=None, password=None):
        # Make sure we have a user and pass
        if not username or not password:
            return None

        l = ldap.initialize(settings.PAPAYA_LDAP_SERVER_URI, bytes_mode=False)
        try:
            ldapuser = "uid=%s,%s" % (username, settings.PAPAYA_LDAP_USERS_DN)
            l.simple_bind_s(ldapuser, password)
            query = self.prepare_query('(uid=%s)', [username])

            uid, entry = l.search_s(settings.PAPAYA_LDAP_USERS_DN, ldap.SCOPE_SUBTREE, query)[0]
        except ldap.LDAPError as e:
            entry = None
            user = None

        if entry:
            # find or create user
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User.objects.create_user(username, entry['mail'][0].decode('utf-8'))

            # update user fiels
            user.first_name = entry['givenName'][0].decode("utf-8")
            user.last_name = entry['sn'][0].decode("utf-8")

            # get groups
            group_results = l.search_s(settings.PAPAYA_LDAP_GROUPS_DN, ldap.SCOPE_SUBTREE, '(objectClass=posixGroup)')
            for uid, entry in group_results:
                if 'cn' in entry and 'memberUid' in entry:
                    groupname = entry['cn'][0].decode('utf-8')

                    # find group
                    try:
                        group = Group.objects.get(name=groupname)
                    except Group.DoesNotExist:
                        group = None

                    member_usernames = [username.decode('utf-8') for username in entry['memberUid']]
                    if user.username in member_usernames:
                        # create group if necessary and add user to it
                        if not group:
                            group = Group.objects.create(name=groupname)
                        user.groups.add(group)
                    else:
                        # remove user from the group
                        user.groups.remove(group)
            user.save()

        l.unbind_s()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
