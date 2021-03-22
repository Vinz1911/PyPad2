<div align="center">
    <h1>
        <br>
            PyPad2
        <br>
    </h1>
</div>

`PyPad2` is simple and easy to use wrapper around `evdev` to read gamepad input from XBOX/PS4 controller

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
from pypad2 import Gamepad, KeymapType, KeymapsPS
```

## Usage:
### Examples:

```python
from pypad2 import Gamepad, KeymapsPS


# read button's and Axe's
def on_keys(keys):
    if KeymapsPS.AXE_L2 in keys:
        print(keys[KeymapsPS.AXE_L2])
    if KeymapsPS.AXE_R2 in keys:
        print(keys[KeymapsPS.AXE_R2])


# callback on successfully established connection
def on_begin():
    print('controller connected & ready')


# callback on error
def on_error(error):
    print(f"error: {error}")


gamepad = Gamepad()                     # create instance
gamepad.on_begin(callback=on_begin)     # assign callback
gamepad.on_keys(callback=on_keys)       # assign callback
gamepad.on_error(callback=on_error)     # assign callback
gamepad.start()                         # read input | this is non-blocking, uses own thread
```

## Author:
👨🏼‍💻 [Vinzenz Weist](https://github.com/Vinz1911)