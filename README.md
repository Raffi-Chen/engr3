




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
For the wiring diagrams, I used <a href="tinkercad.com">TinkerCAD</a>.

### Reflection
Although the wiring was easy due to the exact sameness to Arduino wiring, this assignment was difficult in terms of code due to my inexperience in CircuitPython. Initially, I attempted to copy it word for word from Arduino. I soon discovered that not all commands were the same as Arduino and couldn't be translated exactly, just as English can't be translated word for word to French. For example, you need to import the board to the code in CircuitPython, something that was implied in Arduino. However, I eventually found a few examples in the Adafruit CircuitPython library, and including <a href="https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo">this sketch</a> on servos on CircuitPython (where PWM needs to be integrated with a simple line of command that does all the work for you, and then for statements are needed to actually set servo values) and <a href="https://learn.adafruit.com/multi-tasking-with-circuitpython/buttons">this sketch</a> on buttons (where many of the functions are similar to Arduino but need colons instead of curly brackets, and need to be initiated with digitalio.)





## DistanceSensor

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
Pictures / Gifs of your finished work should go here.  You need to communicate what your thing does.
For making a GIF, I recommend [ezgif.com](https://www.ezgif.com) Remember you can insert pictures using Markdown or HTML to insert an image.


And here is how you should give image credit to someone if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)


### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**





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
<!--For the GIFs, I use <a href="ezgif.com">EzGIF</a>.-->
<!--For the wiring diagrams, I use <a href="tinkercad.com">TinkerCAD</a>.-->
