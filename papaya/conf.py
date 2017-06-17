# -*- coding: utf-8 -*-
#
# papaya
# Copyright (C) 2009-2012 Bolloré telecom
# Copyright (C) 2016 Polyconseil
# See AUTHORS file for a full list of contributors.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import appconf

from django.conf import settings  # noqa: F401


class PapayaConf(appconf.AppConf):
    """Default settings for papaya.

    Override in settings.py.
    """

    class Meta:
        prefix = 'papaya'

    # LDAP Backend
    LDAP_SERVER_URI = 'ldap://localhost'
    LDAP_USERS_DN = None
    LDAP_GROUPS_DN = None

    # OpenID consumer
    CONSUMER_TRUSTED = []
    CONSUMER_REALMS = []

    # OpenID provider
    # list of regexps matching trusted consumers
    SERVER_TRUSTED = []
