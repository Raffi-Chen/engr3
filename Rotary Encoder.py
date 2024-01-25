import rotaryio # Imports value of rotary encoder's turning function to use later
import board # Allows code to relate to certain pins on board
import neopixel # Activates board's neopixel for later use
import digitalio # For use in button (digital values are 1/0 rather than fluid)
from lcd.lcd import LCD # importing lcd stuff below
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2) # Establishes pins of rotary encoder

lcd = LCD(I2CPCF8574Interface(board.I2C(),0x27),num_rows=2,num_cols=16) 
# Begin communication with LCD screen

led = neopixel.NeoPixel(board.NEOPIXEL,1)
led.brightness = 0.1
# Establishes properties of neopixel

button = digitalio.DigitalInOut(board.D2) # Establishes communication with 2nd pin
button.direction = digitalio.Direction.INPUT # Establishes button input
button.pull = digitalio.Pull.UP
button_state = 0

menu = ["stop         ", "caution         ", "go          "] # Used for menu later

menu_index = 0

while True:

    menu_index = enc.position # Menu index is what encoder reads
    menu_index_lcd = menu_index % 3 # Finds remainder of # to read only 1, 2, or 3

    lcd.set_cursor_pos(0,0)
    lcd.print(menu[menu_index_lcd]) # Initiates + displays LCD values "stop", "caution", "go"

    if button.value and button_state == 0:

        print(f"Menu Index = {menu_index_lcd}") # F string allows us to print both text and variable to describe state of menu index with text
        button_state = 1

        if menu_index_lcd is 0:

            led[0] = (255, 0, 0)

        if menu_index_lcd is 1:

            led[0] = (255, 255, 0)

        if menu_index_lcd is 2:

            led[0] = (0, 255, 0) # If then to tell neopixel what to show

    elif not button.value:

        button_state = 0 # Button is not pressed if not pressed