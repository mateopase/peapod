import supervisor
import storage
import usb_cdc


supervisor.set_next_stack_limit(4096 + 4096)


try:
    # Attempt to load the main boot config
    import boot_main
except Exception as boot_exception:
    print(f"Boot setup failed with exception: {boot_exception}")
    print("Enabling console and USB storage.")

    # Enable serial console and USB storage for debugging
    usb_cdc.enable()
    storage.enable_usb_drive()
    
    # Raise caught exception so it's logged in boot_out.txt
    raise boot_exception

