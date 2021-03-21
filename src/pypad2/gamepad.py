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

from evdev import InputDevice, categorize, ecodes
from .keymaps import KeymapType, KeymapsPS, KeymapsXBX
from threading import Thread


class Gamepad:
    def __init__(self, path: str = '/dev/input/event2', pad: KeymapType = KeymapType.PS):
        """
        create instance of gamepad
        :param path: the path to the input, default: '/dev/input/event2'
        :param pad: the keymap type, default: KeymapType.PS
        """
        self.__pad = pad
        self.__path = path
        self.__gamepad = None
        self.__thread = None
        self.__callback_begin = None
        self.__callback_keys = None
        self.__callback_error = None

    def start(self):
        """
        start to read input from path
        """
        try:
            self.__gamepad = InputDevice(self.__path)
        except Exception as error:
            if self.__callback_error:
                self.__callback_error(error)
            return
        self.__thread = Thread(target=self.__read_input)
        self.__thread.start()

    def stop(self):
        """
        stop reading from gamepad
        :return:
        """
        if not self.__gamepad:
            return
        self.__gamepad.close()

    def get_name(self):
        """
        get controller name
        :return: the name of the controller
        """
        if not self.__gamepad:
            return
        return self.__gamepad.name

    def on_begin(self, callback):
        """
        callback on successfully started
        :param callback: callback func
        """
        self.__callback_begin = callback

    def on_keys(self, callback):
        """
        callback on key press
        :param callback: callback func
        """
        self.__callback_keys = callback

    def on_error(self, callback):
        """
        callback on error
        :param callback: callback func
        """
        self.__callback_error = callback

    def __read_input(self):
        """
        input read loop
        """
        try:
            if self.__callback_begin:
                self.__callback_begin()
            for event in self.__gamepad.read_loop():
                self.__map_keys(event)

        except Exception as error:
            self.stop()
            if self.__callback_error:
                self.__callback_error(error)

    def __map_keys(self, event):
        """
        map keys
        :param event: input event
        """
        output = {}
        mapped = None
        if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
            try:
                key = categorize(event)
                if self.__pad == KeymapType.PS:
                    mapped = KeymapsPS(key.event.code)
                if self.__pad == KeymapType.XBX:
                    mapped = KeymapsXBX(key.event.code)
                output[mapped] = key.event.value
                if self.__callback_keys:
                    self.__callback_keys(output)
            except Exception as error:
                if self.__callback_error:
                    self.__callback_error(error)


