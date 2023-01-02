import microcontroller


def reboot_to_bootloader():
    microcontroller.on_next_reset(microcontroller.RunMode.BOOTLOADER)
    microcontroller.reset()


def reboot_to_safe_mode():
    microcontroller.on_next_reset(microcontroller.RunMode.SAFE_MODE)
    microcontroller.reset()
