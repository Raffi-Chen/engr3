import time
import digitalio
from lcd.lcd import LCD
import board
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# Set up photointerrupter on Pin 2
photointerrupter=digitalio.DigitalInOut(board.D2)

# Set up photointerrupter as input
photointerrupter.direction = digitalio.Direction.INPUT

# Use internal pull-up resistor
photointerrupter.pull = digitalio.Pull.UP

# Set photointerrupter_state as None for now
photointerrupter_state = None

while True:
# If photointerrupter interrupted, set photointerrupter_state to "interrupted"
    if photointerrupter.value and photointerrupter_state is None:
        photointerrupter_state = "interrupted"
        print("rgeih8hgeuwq")
    else:
        photointerrupter_state = None

# If interrupted, set state to None, and print that photointerrupter was interrupted to Serial Moniter
# Increase variable called interrupt_counter by 1