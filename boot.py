import supervisor


supervisor.set_next_stack_limit(4096 + 4096)


try:
    import boot_main
except Exception as boot_exception:
    print(f"Boot setup failed with exception: {boot_exception}")
    print("Enabling console and USB storage.")

    try:
        from utils import reboot_to_safe_mode

        reboot_to_safe_mode()
    except:
        import storage
        import usb_cdc

        storage.enable_usb_drive()
        usb_cdc.enable()

        raise boot_exception
