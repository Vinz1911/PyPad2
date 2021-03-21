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

from pypad2 import Gamepad, KeymapType, KeymapsPS


def on_keys(keys):
    if KeymapsPS.AXE_L2 in keys:
        print(keys[KeymapsPS.AXE_L2])
    if KeymapsPS.AXE_R2 in keys:
        print(keys[KeymapsPS.AXE_R2])


def on_begin():
    print('controller connected & ready')


def on_error(error):
    print(f"error: {error}")


gamepad = Gamepad(path='/dev/input/event2', pad=KeymapType.PS)
gamepad.on_begin(callback=on_begin)
gamepad.on_keys(callback=on_keys)
gamepad.on_error(callback=on_error)
gamepad.start()
print('start')