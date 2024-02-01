import time
import digitalio
from lcd.lcd import LCD
import board
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

interrupt_counter = 0

lcd = LCD(I2CPCF8574Interface(board.I2C(),0x27),num_rows=2,num_cols=16)

photointerrupter=digitalio.DigitalInOut(board.D2) # Set up photointerrupter on Pin 2
photointerrupter.direction = digitalio.Direction.INPUT # Set up photointerrupter as input
photointerrupter.pull = digitalio.Pull.UP # Use internal pull-up resistor
photointerrupter_state = 0 # Set photointerrupter_state as None for now

now = time.monotonic() # Time in seconds since power on

lcd.set_cursor_pos(0,0)
lcd.print("Interrupt Count:")
lcd.set_cursor_pos(1,0)
lcd.print(str(interrupt_counter))

while True:
    if (now + 4) < time.monotonic(): # If 4 seconds elapses

        print("done")
        now = time.monotonic()
        lcd.set_cursor_pos(0,0)
        lcd.print("Interrupt Count:")
        lcd.set_cursor_pos(1,0)
        lcd.print(str(interrupt_counter))

    if photointerrupter.value == True:
        if photointerrupter_state == 0: # If photointerrupter interrupted, set photointerrupter_state to "interrupted"

            photointerrupter_state = 1
            interrupt_counter = interrupt_counter + 1
    
    else:
        photointerrupter_state = 0