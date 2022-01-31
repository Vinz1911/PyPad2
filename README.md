<div align="center">
    <h1>
        <br>
            PyPad2
        <br>
    </h1>
</div>

`PyPad2` is simple and easy to use wrapper around `evdev` to read gamepad input from PS4 controller

## License:
[![License](https://img.shields.io/badge/license-GPLv3-blue.svg?longCache=true&style=flat)](https://github.com/Vinz1911/PyPad2/blob/master/LICENSE)

## Python & Pypi:
[![Python](https://img.shields.io/badge/Python-v3.8-blue.svg?logo=python&style=flat)](https://www.python.org) [![PyPi](https://img.shields.io/badge/PyPi-Support-blue.svg?logo=pypi&style=flat)](https://pypi.org)

## Install & Upgrade:
```shell
# install via pypi
pip3 install pypad2
# upgrade
pip3 install --upgrade pypad2
```

## Import:

```python
from pypad2 import Gamepad, Keymap
```

## Usage:
### Examples:

```python
from pypad2 import Gamepad, Keymap

# create instance
gamepad = Gamepad(path='/dev/input/event2')

# get gamepad's name
name = gamepad.name()
print(name)

# get gamepad's status
status = gamepad.status()
print(status)  # print's: {'capacity': '100', 'status': 'Discharging'}

# set gamepad's color
gamepad.color()

while True:
    buttons = gamepad.pressed()
    for button in buttons:
        print(f'{button.name}: {buttons[button]}')
```

## Author:
👨🏼‍💻 [Vinzenz Weist](https://github.com/Vinz1911)