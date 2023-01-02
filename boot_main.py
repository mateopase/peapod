import digitalio
import storage
import usb_cdc
import usb_hid
import usb_midi

from kb import Peapod


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


# Immediaately reboot to bootloader if Q is pressed
if get_switch(BOOTLOADER_KEY):
    import microcontroller

    microcontroller.on_next_reset(microcontroller.RunMode.BOOTLOADER)
    microcontroller.reset()


# Continue boot w/ development enabled if P is pressed
if get_switch(DEV_KEY):
    print("Booting in development mode. USB storage and serial console enabled.")
    usb_cdc.enable()
    usb_midi.disable()
    storage.enable_usb_drive()
else:
    usb_cdc.disable()
    usb_midi.disable()
    storage.disable_usb_drive()
    usb_hid.enable((usb_hid.Device.KEYBOARD,), boot_device=1)

