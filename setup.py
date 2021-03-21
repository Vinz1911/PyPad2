#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Setup
#
# Copyright (C) 2020 Vinzenz Weist Vinz1911@gmail.com
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__author__ = "Vinzenz Weist"
__copyright__ = "Copyright 2020, Vinzenz Weist"
__license__ = "GPLv3"
__version__ = "0.0.9"

from setuptools import setup

setup(
    name='pypad2',
    version='0.0.9',
    packages=['pypad2'],
    package_dir={'': 'src'},
    license='GPLv3',
    description='Python Gamepad',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    url='https://github.com/Vinz1911/PyPad2',
    author='Vinzenz Weist',
    author_email='Vinz1911@gmail.com',
    install_requires=['evdev']
)