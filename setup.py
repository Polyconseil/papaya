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
