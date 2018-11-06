#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright (C) 2018 Matthias Luescher
#
# Authors:
#  Matthias Luescher
#
# This file is part of edi-boot-shim.
#
# edi-boot-shim is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# edi-boot-shim is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with edi-boot-shim.  If not, see <http://www.gnu.org/licenses/>.

# setup.py according to
# http://python-packaging-user-guide.readthedocs.io/en/latest/distributing/

from setuptools import setup, find_packages
from codecs import open
from os import path
from pip.req import parse_requirements
import glob
import os

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


def get_install_requires():
    install_reqs = parse_requirements("requirements.txt", session=False)
    return [str(ir.req) for ir in install_reqs]


setup(
    name='edi-boot-shim',

    version='0.1.1+deb9',

    description='edi Boot Shim',
    long_description=long_description,

    url='https://github.com/lueschem/edi-boot-shim',

    # Author details
    author='Matthias Luescher',
    author_email='lueschem@gmail.com',

    # Choose your license
    license='GPLv3+',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='embedded Linux container toolchain lxd lxc Ansible Debian',

    packages=find_packages(exclude=['docs', 'debian', 'bin', '.git']),

    install_requires=get_install_requires(),

    extras_require={
        # 'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },

    package_data={
    },

    data_files=[('/etc/edi-boot-shim/', ['templates/boot.cmd.j2'])],

    entry_points={
        'console_scripts': [
            'edi-boot-shim=edi_boot_shim:main',
        ],
    },
)
