import rotaryio
import board
import neopixel
import digitalio
from lcd.lcd import LCD # importing lcd stuff below
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import busio
import time

enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2)

lcd = LCD(I2CPCF8574Interface(board.I2C(),0x27),num_rows=2,num_cols=16) 
# Begin communication with LCD screen
#i2c = busio.I2C(board.SCL,board.SDA)

led = neopixel.NeoPixel(board.NEOPIXEL,1)
led.brightness = 0.3
# Establishes properties of neopixel

button = digitalio.DigitalInOut(board.D2) # Establishes communication with 2nd pin
button.direction = digitalio.Direction.INPUT # Establishes button input
button.pull = digitalio.Pull.UP
button_state = None

while True:

    lcd.print("!23123") # Prints value to LCD screen
    led[0] = (255, 0, 0) # Projects certain color to LED

    if not button.value and button_state is None: # If button value is NOT 0 (if it is 1/pressed)
        button_state = "pressed"
    if button.value and button_state == "pressed":
        print("Button is pressed")
        button_state = None