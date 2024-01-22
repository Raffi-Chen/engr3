import board
import neopixel
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

led = neopixel.NeoPixel(board.NEOPIXEL,1)
led.brightness = 0.1

while True:
    led[0] = (255, 0, 0)