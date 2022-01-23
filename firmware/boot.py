import supervisor

supervisor.set_next_stack_limit(4096 + 4096)

import storage, usb_cdc
import board, digitalio

# initialize row 0 as output
row = digitalio.DigitalInOut(board.D2)
row.direction = digitalio.Direction.OUTPUT

# initialize col 4 as input in pulldown mode
col = digitalio.DigitalInOut(board.D10)
col.pull = digitalio.Pull.DOWN

# set row state HIGH
row.value = True

# disable developer mode unless dash is pressed
if not button.value:
  storage.disable_usb_drive()
  usb_cdc.disable()
