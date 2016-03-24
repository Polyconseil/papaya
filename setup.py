#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from papaya.version import VERSION


def read(filename):
    with open(filename) as fp:
        return fp.read()


setup(
    name="papaya",
    version=VERSION,
    author="Polyconseil Sysadmin Team",
    author_email="sysadmin+papaya@polyconseil.fr",
    description="A LDAP-based django authentication provider, with openid.",
    license="GPL",
    keywords=['papaya', 'ldap', 'authentication', 'django', 'openid'],
    url="https://github.com/Polyconseil/papaya",
    packages=find_packages(),
    long_description=read('README.rst'),
    install_requires=[
        # Django core
        'Django>=1.7,<1.8',

        # Databases
        'pyldap<2.5',

        # Configuration
        'django-appconf',

        # OpenID
        'openid',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Environment :: Console",
        "Framework :: Django",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 2.7",
        "Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP",
    ],
    include_package_data=True,
)
