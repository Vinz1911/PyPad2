#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# main.py
#
# Copyright (C) 2020-2022 Vinzenz Weist Vinz1911@gmail.com
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

from src.pypad2 import Gamepad
import time

try:
    gamepad = Gamepad(path='/dev/input/event2')
    print(gamepad.name())
    print(gamepad.status())
    gamepad.color(0, 255, 255)
    while True:
        buttons = gamepad.pressed()
        for button in buttons:
            print(f'{button.name}: {buttons[button]}')

        time.sleep(0.016)

except Exception as error:
    print(f'[ERROR]: {error}')
