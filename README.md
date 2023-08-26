# peapod
This is a dump of the source code for a hand-wired 30-key ortholinear keyboard.
The case was printed on an SLA printer from clear resin (for maximum wire visibility).

## Overview
This keyboard runs off an rp2040 mcu (the seeed xiao variant specifically).
It's using the fantastic [KMK keyboard firmware](https://github.com/KMKfw/kmk_firmware),
running on top of CircuitPython.

## Future Work
Finish the keymap. It's hard to make a functional keyboard in 30 keys.
Maybe writers will be interested since 30 keys is enough to support:
- 26 letters
- shift
- backspace
- enter
- space

And I guess a double space could input a period or something like that.
No commas allowed.
