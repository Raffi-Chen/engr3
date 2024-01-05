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
i2c = busio.I2C(board.SCL,board.SDA)

led = neopixel.NeoPixel(board.NEOPIXEL,1)
led.brightness = 0.3

while True:

    led[0] = (255, 0, 0)
    
    print("I2C addresses found:", [hex(device_address) for device_address in i2c.scan()])
    time.sleep(2)
'''
while not i2c.try_lock() :
    pass

# comment
'''