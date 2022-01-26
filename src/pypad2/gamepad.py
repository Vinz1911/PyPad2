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

from evdev import InputDevice, ecodes
from .keymaps import Keymap
from threading import Thread


class Gamepad:
    """
    create a gamepad device which can read input
    from Playstation(R) 4 Controller
    :param path: the device input path
    """
    def __init__(self, path: str = '/dev/input/event2'):
        self.__input: InputDevice = None
        self.__path: str = path
        self.__buttons: dict = {}
        self.__thread = Thread(target=self.__read_input, daemon=True)
        self.__open()

    def pressed(self) -> {}:
        """
        read the input device's pressed buttons
        :return: the pressed buttons
        """
        return self.__buttons

    def name(self) -> str:
        """
        read the input device's friendly name
        :return: the name of the input deice
        """
        if not self.__input: return str()
        return self.__input.name

    def __open(self):
        try:
            self.__input = InputDevice(self.__path)
            for entry in Keymap: self.__buttons[entry] = 0
            self.__thread.start()
        except Exception as error:
            print(f'[ERROR]: {error}')

    def __read_input(self):
        input_events = self.__input.read_loop()
        for event in input_events:
            if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                self.__buttons[Keymap(event.code)] = event.value
