import microcontroller
import storage
import usb_cdc
import usb_hid
import usb_midi


def reboot_to_bootloader():
    microcontroller.on_next_reset(microcontroller.RunMode.BOOTLOADER)
    microcontroller.reset()


def reboot_to_safe_mode():
    microcontroller.on_next_reset(microcontroller.RunMode.SAFE_MODE)
    microcontroller.reset()


def enable_dev_mode():
    print("Enabling development mode. USB storage and serial console enabled.")
    usb_cdc.enable()
    usb_midi.disable()
    storage.enable_usb_drive()


def enable_keyboard_mode():
    usb_cdc.disable()
    usb_midi.disable()
    storage.disable_usb_drive()
    usb_hid.enable((usb_hid.Device.KEYBOARD,), boot_device=1)
