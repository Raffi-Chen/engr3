




# CircuitPython
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [RGB LED](#RGBLED)
* [CircuitPython Servo](#CircuitPythonServo)
* [Distance Sensor](#DistanceSensor)
* [NextAssignmentGoesHere](#NextAssignment)
---





## RGBLED

### Description & Code Snippets
The purpose of this assignment was to use the neopixel in the microcontroller to rotate between the colors of the rainbow. To go about this assignment, I used a code library and edited it accordingly.

```python
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
```
<a href="https://github.com/Raffi-Chen/engr3/blob/main/RGBLED.py">Link to code</a><br>
Referenced from <a href="https://circuitpython.org/libraries">the CircuitPython Library</a>

### Evidence
https://github.com/Raffi-Chen/engr3/assets/143544930/a6bfe0a4-c372-40e4-89a4-0efd6942b04f

### Wiring
There is no wiring diagram for this assignment, as the neopixel is already integrated into the Metro board.

### Reflection
Before we started this assignment, we were not given any code or wiring. That didn't work well, as conversion from Arduino to CircuitPython can be painful and can not be translated word for word. However, Mr. Helmstetter soon realized that that was a quite difficult starting point in CircuitPython, and we were instead told to use the neopixel on the Metro board as well as the code given on the CircuitPython library. That definitely did make things much easier, but it didn't completely get rid of every single difficulty. First of all, the NUMPIXELS value in the variables needed to be changed to match the Metro. Although this is not a difficult thing to change, I didn't understand what it meant and tried many values. The speed and brightness values were self-explanatory, but the PIN value was confusing because I had to say board.NEOPIXEL rather than any pin actually on the board. In this aspect, I got help from classmates to get to my solution. While documenting it, I found that my colors couldn't change normally! This was due to the fact that the neopixel aspect of the board was not integrated into my GitHub library, and worked afterwards.





## CircuitPythonServo

### Description & Code Snippets
The goal of this asignment was to use two buttons to control the direction of a servo. This was the more significant initial endeavor into CircuitPython, as the code was not provided up front. I used code libraries provided by the examples folder we downloaded earlier this year, as well as internet examples, to help.


Using a button requires a lot more than Arduino did

```python
import digitalio

# define pins for each button
pin = digitalio.DigitalInOut(board.D1)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP

button_state = False

while True:
    # if left button pressed
    if pin.value:
        print("Left")
```
Servo code is very similar to arduino, and not worth mentioning here.   If you want to see servo code, just click my code link below:

<a href="https://github.com/Raffi-Chen/engr3/blob/main/Servo.py"> Here is the link to the code displayed. </a>

### Evidence
<img src="ezgif-1-dd8df80974.gif" alt="servo gif">
For the GIFs, I use <a href="ezgif.com">EzGIF</a>.

### Wiring
<img src="Brave Migelo-Krunk.png" alt="wiring diagram">
For the wiring diagrams, I used <a href="tinkercad.com">TinkerCAD</a>. Also, I used a Metro Express instead of an Arduino Uno.

### Reflection
Although the wiring was easy due to the exact sameness to Arduino wiring, this assignment was difficult in terms of code due to my inexperience in CircuitPython. Initially, I attempted to copy it word for word from Arduino. I soon discovered that not all commands were the same as Arduino and couldn't be translated exactly, just as English can't be translated word for word to French. For example, you need to import the board to the code in CircuitPython, something that was implied in Arduino. However, I eventually found a few examples in the Adafruit CircuitPython library, and including <a href="https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo">this sketch</a> on servos on CircuitPython (where PWM needs to be integrated with a simple line of command that does all the work for you, and then for statements are needed to actually set servo values) and <a href="https://learn.adafruit.com/multi-tasking-with-circuitpython/buttons">this sketch</a> on buttons (where many of the functions are similar to Arduino but need colons instead of curly brackets, and need to be initiated with digitalio.)





## DistanceSensor

### Description & Code Snippets
The goal of this assignment was to smoothly enable the neopixel to change based on values detected by the distance sensor, going from red at 5 cm away to green at 35 cm away. There were many resources I needed for this assignment, including library code, past documentation, and not least, Mr. Dierolf's great tips.

There were many components of this assignment, and the code was especially complex due to the intended smoothness of the neopixel.
```python
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
         # map function: simpleio.map_range(x,in_min,in_max,out_min,out_max)
         # using map function for smooth color change
        print(DIST) 
        if DIST < 5: # red
            pixel.fill((255,0,0))
                # need double parentheses to say rgb is a single value
        elif DIST > 5 and DIST < 20:
            pixel.fill((RED1,0,BLUE1))
            # dynamic values btwn red and blue
     pixel.show()
```

The full code link can be found here:

<a href="https://github.com/Raffi-Chen/engr3/blob/main/DiSTanceSenSor.py">Distance Sensor Code</a>

### Evidence
https://github.com/Raffi-Chen/engr3/assets/143544930/bc7d8c38-34e1-43e1-b842-2ada27968b68

### Wiring
![Swanky Bojo-Maimu](https://github.com/Raffi-Chen/engr3/assets/143544930/8f2df754-6d6c-4144-8abb-f2df8e562c0f)
For the wiring diagrams, I used <a href="tinkercad.com">TinkerCAD</a>. Also, I used a Metro Express instead of an Arduino Uno.

### Reflection

I went through this assignment step by step, exactly as it was displayed on the assignment. <br><br>
Step 1 was to initiate the distance sensor with CircuitPython, by which I could make use of <a href="https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/main/examples/hcsr04_simpletest.py">Adafruit library code</a> on. On this step, I felt as if I were simply having trouble because the distance sensor was drawing too much energy from the Metro. Eventually, Mr. Helmstetter realized that it was the circumstances of the current version of CircuitPython (v 8) didn't support distance sensors well, and everyone in the class switched to version 7.<br><br>
Step 2 was to get the neopixel to change red at less than 5 cm and green at more than 35 cm. I had relatively less trouble on this stage, but I still had to reference the previous neopixel code for a while to remember the ins and outs of CircuitPython. This displays the importance of documentation.<br><br>
Step 3 was to get the light to smoothly shift colors. As with many things, it's something that sounds inaccessible but is actually quite simple when you break it into steps. For this particular step, the map() feature was needed in order to seamlessly change colors based on certain distances. This required my <a href="https://sites.google.com/charlottesvilleschools.org/rcengii/not-so-basic-arduino/ultrasonic-rangefinder">previous documentation</a>, as I forgot how a map() functioned. After this tedious code step, I ran into many errors, including the fact that I needed to define the RGB values as a single value on line 39/42/45/47/50, and the fact that I forgot to upload simpleio into my CircuitPython library.

## NextAssignment

### Description & Code Snippets
Write a couple sentences here, describing this assignment, and make sure that you hit these two points:
* What was the goal of the assignment?
* How did you accomplish that goal?
  How you accomplished the goal is NOT a reflection, it is you telling the reader how to do this assignment, in broad strokes.

  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
Code goes here

```

**Lastly, please end this section with a link to your code or file.**  

### Evidence

### Wiring
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)
### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**
<br><br><br>

<!--References for commonly used sources-->
<!--For the wiring diagrams, I use <a href="tinkercad.com">TinkerCAD</a>.-->
