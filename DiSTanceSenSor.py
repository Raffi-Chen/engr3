# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT  

import time
import board
import adafruit_hcsr04
from rainbowio import colorwheel
import neopixel
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

DIST = sonar.distance
MAP = simpleio.map_range

NUMPIXELS = 1
BRIGHTNESS = 0.05
PIN = board.NEOPIXEL
RED1 = MAP(DIST,255,0,5,20)
BLUE1 = MAP(DIST,0,255,5,20)
GREEN2 = MAP(DIST,0,255,20,35)
BLUE2 = MAP(DIST,255,0,20,35)

# map function: simpleio.map_range(x,in_min,in_max,out_min,out_max)

pixel = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS)

while True:
    try:
        print(DIST) 
        if DIST < 5: # red
            pixel.fill(255,0,0)
        elif DIST > 5 and DIST < 20:
            pixel.fill(RED1,0,BLUE1)
        elif DIST == 20: # blue
            pixel.fill(0,0,255)
        elif DIST > 20 and DIST < 35:
            pixel.fill(0,GREEN2,BLUE2)
        elif DIST > 35: # green
            pixel.fill(0,255,0)

    except RuntimeError:
        print("Retrying!")
        time.sleep(0.5)


''' Neopixel code for reference
from rainbowio import colorwheel
import neopixel

NUMPIXELS = 1  # Update this to match the number of LEDs.
SPEED = 0.05  # Increase to slow down the rainbow. Decrease to speed it up.
BRIGHTNESS = 0.05  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.NEOPIXEL  # This is the default pin on the 5x5 NeoPixel Grid BFF.

pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)


def rainbow_cycle(wait):
    for color in range(255):
        for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
            pixel_index = (pixel * 256 // len(pixels)) + color * 5
            pixels[pixel] = colorwheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

while True:
    rainbow_cycle(SPEED)'''