# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT  

import time
import board
import adafruit_hcsr04
from rainbowio import colorwheel
import neopixel
import simpleio # need to make sure these components are uploaded onto library
# upload essential components of code: for arduino and initiation for components of code

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
# initiate distance sensor values

NUMPIXELS = 1
BRIGHTNESS = 0.05
PIN = board.NEOPIXEL
# values needed for neopixel

pixel = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS)
# setup of neopixel

while True:

    try: # try so error does not occur - if not true go to runtime error

        DIST = sonar.distance
        MAP = simpleio.map_range

        RED1 = MAP(DIST,5,20,255,0)
        BLUE1 = MAP(DIST,5,20,0,255)
        GREEN2 = MAP(DIST,20,35,0,255)
        BLUE2 = MAP(DIST,20,35,255,0)
         # map function: simpleio.map_range(x,in_min,in_max,out_min,out_max)
         # using map function for smooth color change

        print(DIST) 
        if DIST < 5: # red
            pixel.fill((255,0,0))
                # need double parentheses to say rgb is a single value
        elif DIST > 5 and DIST < 20:
            pixel.fill((RED1,0,BLUE1))
            # dynamic values btwn red and blue
        elif DIST == 20: # blue
            pixel.fill((0,0,255))
        elif DIST > 20 and DIST < 35:
            pixel.fill((0,GREEN2,BLUE2))
            # dynamic values btwn blue and green
        elif DIST > 35: # green
            pixel.fill((0,255,0))
        pixel.show()

    except RuntimeError:
        print("Retrying!")
