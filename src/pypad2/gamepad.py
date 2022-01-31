#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# gamepad.py
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

from evdev import InputDevice, ecodes
from .keymaps import Keymap
from threading import Thread
from glob import glob


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

    def pressed(self) -> dict:
        """
        read the input device's pressed buttons
        :return: the pressed buttons
        """
        return self.__buttons

    def name(self) -> str:
        """
        read the input device's friendly name
        :return: the name of the input device
        """
        if not self.__input: return str()
        return self.__input.name

    def color(self, red: int, green: int, blue: int):
        """
        change the color of the input device
        :param red: brightness from 0-255
        :param green: brightness from 0-255
        :param blue: brightness from 0-255
        """
        colors = ['red', 'green', 'blue']
        for color in colors:
            for path in glob(f'/sys/class/leds/0005:054C:*:{color}'):
                if color == 'red': f = open(path + '/brightness', 'a'); f.write(str(red)); f.close()
                if color == 'green': f = open(path + '/brightness', 'a'); f.write(str(green)); f.close()
                if color == 'blue': f = open(path + '/brightness', 'a'); f.write(str(blue)); f.close()

    def status(self) -> dict:
        """
        get the input device's status
        :return: dictionary with capacity and charging status
        """
        status = {'capacity': '', 'status': ''}
        for path in glob('/sys/class/power_supply/sony_controller_battery_*'):
            for state in status: f = open(path + '/' + state, "r"); status[state] = str(f.read()).rstrip() ; f.close()
        return status

    # MARK: - Private API -

    def __open(self):
        self.__input = InputDevice(self.__path)
        for entry in Keymap: self.__buttons[entry] = 0
        self.__thread.start()

    def __read_input(self):
        try:
            input_events = self.__input.read_loop()
            for event in input_events:
                if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                    self.__buttons[Keymap(event.code)] = event.value
        except:
            self.__buttons = None
            self.__input.close()
