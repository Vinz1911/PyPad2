#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# keymaps.py
#
# Copyright (C) 2022 Vinzenz Weist Vinz1911@gmail.com
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

from enum import Enum


class Keymap(Enum):
    BTN_CROSS = 304
    BTN_CIRCLE = 305
    BTN_TRIANGLE = 307
    BTN_SQUARE = 308

    BTN_L1 = 310
    BTN_R1 = 311
    BTN_L2 = 312
    BTN_R2 = 313
    BTN_LT = 317
    BTN_RT = 318

    BTN_SHARE = 314
    BTN_OPTIONS = 315
    BTN_PS = 316

    AXE_LX = 0
    AXE_LY = 1
    AXE_RX = 3
    AXE_RY = 4

    AXE_L2 = 2
    AXE_R2 = 5

    AXE_DX = 16
    AXE_DY = 17
