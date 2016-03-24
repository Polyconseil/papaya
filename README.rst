granadilla
==========

This django-backed software provides a simple administration tool for a minimal LDAP directory:

* Web application providing a clean, editable phonebook (including pictures)
* Command-line tool to manage users and groups

It has been designed for the specific LDAP setup at Polyconseil, but could be useful to other teams/companies.

Configuration
-------------

The webapp can run either in a standalone mode (with the ``granadilla_webapp.settings`` setup)
or integrated in a larger website; the required settings are listed in ``granadilla/conf.py``.

The command-line tool is designed for standalone use, and reads its settings from the ``/etc/granadilla/settings.ini`` file.
This file is also used by the webapp if launched in standalone mode, with ``DJANGO_SETTINGS_MODULE=granadilla_webapp.settings``.

The valid configuration values are described in the ``example_settings.ini`` file.



License
-------

Copyright (C) 2009 Bolloré telecom
Copyright (C) 2014 Polyconseil
See AUTHORS file for a full list of contributors.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

