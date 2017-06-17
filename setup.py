#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import codecs
import os
import re
import sys

from setuptools import find_packages, setup

root_dir = os.path.abspath(os.path.dirname(__file__))


def get_version(package_name):
    version_re = re.compile(r"^VERSION = [\"']([\w_.-]+)[\"']$")
    package_components = package_name.split('.')
    init_path = os.path.join(root_dir, *(package_components + ['version.py']))
    with codecs.open(init_path, 'r', 'utf-8') as f:
        for line in f:
            match = version_re.match(line[:-1])
            if match:
                return match.groups()[0]
    return '0.1.0'


PACKAGE = 'papaya'


setup(
    name=PACKAGE,
    version=get_version(PACKAGE),
    author="Polyconseil Sysadmin Team",
    author_email="sysadmin+%s@polyconseil.fr" % PACKAGE,
    description="A LDAP-based django authentication provider, with openid.",
    license="GPL",
    keywords=['papaya', 'ldap', 'authentication', 'django', 'openid'],
    url="https://github.com/Polyconseil/%s" % PACKAGE,
    packages=find_packages(exclude=['tests*', 'dev']),
    long_description=''.join(codecs.open('README.rst', 'r', 'utf-8').readlines()),
    install_requires=[
        # Django core
        'Django>=1.11',

        # Databases
        'pyldap',

        # Configuration
        'django-appconf',

        # OpenID
        'python-openid',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Framework :: Django :: 1.11",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP",
    ],
    include_package_data=True,
)
