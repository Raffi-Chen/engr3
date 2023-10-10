




# CircuitPython AND Onshape
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [RGB LED](#RGBLED)
* [CircuitPython Servo](#CircuitPythonServo)
* [Distance Sensor](#DistanceSensor)
* [Motor Control](#MotorControl)
* [The Hanger - ONSHAPE](#TheHanger)
* [Swing Arm - ONSHAPE](#SwingArm)
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
<br><br><br>





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
<br><br><br>





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
<br><br><br>





## MotorControl

### Description & Code Snippets
In this assignment, a potentiometer needed to be utilized in order to control the speed of a DC Motor. The wiring was referenced from a schematic shown on Canvas (which needed to be slightly adjusted), as well as a reference given by Mr. Miller for the code.

```python
pot = analogio.AnalogIn(board.A1) # initialize analog input for potentiometer
motor = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=5000) # use pwm output to pin 3 for motor

while True:
        motor.duty_cycle=(pot.value) # set motor to potentiometer input
```

The full code link can be found <a href="https://github.com/Raffi-Chen/engr3/blob/main/MotorControl.py">here</a>

### Evidence
https://github.com/Raffi-Chen/engr3/assets/143544930/ab053d91-6780-4e27-95f1-ee6d9b387852

### Wiring
I used [tinkercad.com](https://www.tinkercad.com/learn/circuits) for wiring. Note that a Metro was used rather than an Arduino, a prototyping shield instead of a breadboard, and a IRLB8721 transistor rather than an NPN.
![Motor Control](https://github.com/Raffi-Chen/engr3/assets/143544930/0b237101-15be-401b-962d-b8edafb0ddf3)

### Reflection
At the start of this assignment, complicated wiring needed to be figured out. This was provided by the Canvas assignment, however, it was still troublesome. Even though I could easily understand a wire with multiple branches on the wiring diagram, I got confused quickly as to where I was. This eventually led me to make my wiring diagram <i>first</i>, making it simpler to understand immediately (this is using your own documentation to help yourself in the process!) After the extremely tedious wiring stage that spanned a few days due to its complexity (despite having many comprehendable small sections), I got started on the code and got lost immediately, even to the tips to follow analogio and pwmio, subsequently followed by a motor.duty_cycle command, were quite straightforward. My code is generally self explanatory now that I look at it, however, there are several strange problems I ran into. Initially, I used A3 instead of D3 to denote my motor pin, showing how important it is to reread through your code carefully. My potentiometer was reading astonishingly low numbers such as 1300, whereas the maximum values should have been around 65000. We then realized that the potentiometer was missing a pin, deeming it unusable. This definitely shows how many faults in Arduino could be beyond our control! Finally, my code was initially reading too many outliers, and I solved this simply by firming the position of the pins in relation to where they were plugged into. The errors in this assignment did seem quite random, however, they made me realize how cruicial it is to check all components of a project/assignment that could be malfunctioning. Another thing I see thoroughout all learning: you never learn until you're finished, when you see that something works. That's the way "learning by doing" effectively happens in all Engineering classes here.
<br><br><br>





## TheHanger

### Assignment Description
This was an Onshape practice sketch, so the purpose was just to copy off the components of the sketch. This sketch which was to be made is apparently known as "The Hanger," which appears to be a bridge-like shape that can hang objects. According to Mr. Miller, though, the function of the item is to improve your Onshape skills.

### Evidence
<img src="https://github.com/Raffi-Chen/engr3/assets/143544930/6616e690-ea7f-47b5-8009-b17f7dc185fd" height="400"><br>
Full isometric view of part<br>
<img src="https://github.com/Raffi-Chen/engr3/assets/143544930/d66a313d-7e26-46a4-ad0c-fa721ac2f842" height="400"><br>
Farther right view, to see holes and specifications more easily<br>

### Part Link 
<a href="https://cvilleschools.onshape.com/documents/865f96fed0da609fd9c53ca2/w/2d679a4153164281520fe900/e/57a5a1dd18376062231b898a?renderMode=0&uiState=6525a21d2b7a2b2847f0aaf6">Link to document can be found here.</a> 

### Reflection
This assignment was inherently challenging despite its simplicity, because I don't really have much practice with Onshape part practice. Although I have done some part challenges in the past, they were <a href="https://cvilleschools.onshape.com/documents/fa13f1659452ebd4119a46b0/w/29409880bc5d85d5be054b02/e/5c57b97836a4be618a435484?renderMode=0&uiState=6525a33d8570735bdd0fa77b">much simpler</a> and could be figured out much more quickly, due to their lack of necessity for mulitiple views. I decided to work from one of the long sides according to the <a href="https://cvilleschools.onshape.com/documents/865f96fed0da609fd9c53ca2/w/2d679a4153164281520fe900/e/536561e7e301dfd13b628e8a">reference I was working off of.</a> This could be easily figured out, however, I needed to figure out a few simple tricks, such as starting off with only the left side so I can mirror the entire thing later. Another thing I needed to figure out was how much to fillet each section that was filleted. This is represented by using the fillet feature (e.g. for the 8 corresponding areas in 8x R8). I also learned to use the hole feature according to the schematic. This is done when a hole around a certain point has many features around it, and can be made by changing the features according to what is defined by the hole function on the schematic.





## SwingArm

### Assignment Description
Like the last assignment, the purpose was simply to copy off the sketches given to make a more complex part off of these drawings. One difficulty was the presence of different dimensions on different sketches, which can test understanding of cutouts and dimensions from different views. However, there was also more help in this assignment in a video from Mr. Miller.

### Evidence
<img src="https://github.com/Raffi-Chen/engr3/assets/143544930/d701157f-250c-4805-94d7-10b420760163" height="400"><br>
Full isometric view of part<br>
<img src="https://github.com/Raffi-Chen/engr3/assets/143544930/dfe05f6d-26a5-4068-9dfd-6a65e0db6148" height="400"><br>
Top view to see detail of section 

### Part Link 
<a href="https://cvilleschools.onshape.com/documents/87bffe9447026db45f302eb6/w/6d108b8a0e10725d961a7657/e/c86c69a80590d6f2071d9697?renderMode=0&uiState=6525a8937e5e2c1b5651cb35">Link to document can be found here.</a>

### Reflection
I had lots more trouble on this assignment than the previous one, mainly because it was extremely difficult to make sense of the different views of the Swing Arm. Inititally, I based my drawing fully off of the <a href="https://cvilleschools.onshape.com/documents/87bffe9447026db45f302eb6/w/6d108b8a0e10725d961a7657/e/35e31da1f85bda7b169e2f7c">front view</a> (or more lika a single perspective on the front view). This excluded many essential components: all aspects of the lengths of each dimension. This crazy drawing was not coherent in places, did not look very close to the actual drawing, and did not follow many of the correct dimensions. (I could take a very long time to describe the faults of this sketch, and frankly, I can't remember them either.) After the huge magnitude of problems with it, I decided I needed to start the assignment over and saw the video, which guided on every step of the assignment. This helped me realize that sometimes, it's more important to go the suggested direction than an apparently useful direction (getting it right the first time). In the end, I didn't learn much more than was obvious the first time: look at all the information you are given and use it to your advantage, as everything is there for a reason. However, I learned from the simplicity of this assignment that sometimes, taking shortcuts is too evasive and doesn't work to result in the desired product.





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
