import digitalio

from peapod import Peapod
from utils import (
    enable_dev_mode,
    enable_keyboard_mode,
    reboot_to_bootloader
)


BOOTLOADER_KEY = (0, 0)  # Q
DEV_KEY = (4, 1)  # P


def get_switch(coord: tuple) -> bool:
    """
    Take a (col, row) tuple and returns the state of the switch at that position.
    True == pressed.
    """
    
    col = digitalio.DigitalInOut(Peapod.col_pins[coord[0]])
    row = digitalio.DigitalInOut(Peapod.row_pins[coord[1]])

    col.switch_to_output(value=True)
    row.switch_to_input(pull=digitalio.Pull.DOWN)

    value = bool(row.value)

    col.deinit()
    row.deinit()

    return value


if get_switch(BOOTLOADER_KEY):
    # Immediaately reboot to bootloader if Q is pressed
    reboot_to_bootloader()
elif get_switch(DEV_KEY):
    # Continue boot w/ development enabled if P is pressed
    enable_dev_mode()
else:
    enable_keyboard_mode()
