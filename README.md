<!--<style>
    a {
        target="_blank";
    }
</style>-->




# CircuitPython AND Onshape
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)

### Engineering III
* [Arduino: RGB LED](#RGBLED)
* [Arduino: CircuitPython Servo](#CircuitPythonServo)
* [Arduino: Distance Sensor](#DistanceSensor)
* [Arduino: Motor Control](#MotorControl)
* [Onshape: The Hanger](#TheHanger)
* [Onshape: Swing Arm](#SwingArm)
* [Onshape: Multipart Cylinder](#MultipartCylinder)
* [Onshape: V Block](#VBlock)
* [Onshape: Alignment Plate](#AlignmentPlate)
* [Onshape: Microphone Stand](#MicrophoneStand)
* [Onshape: Pliers](#Pliers)
* [Arduino: Rotary Encoder](#RotaryEncoder)
* [Arduino: Photointerrupters](#Photointerrupters)
* [Arduino: Stepper Motors](#StepperMotors)
* [Arduino: IR Sensors](#IRSensors)
* [Onshape: Robot Gripper](#RobotGripper)
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
<a href="https://cvilleschools.onshape.com/documents/865f96fed0da609fd9c53ca2/w/2d679a4153164281520fe900/e/57a5a1dd18376062231b898a?renderMode=0&uiState=65528bca19ebf955f955940f">Link to part</a>

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





## MultipartCylinder

### Assignment Description
This assignment's concept is essentially the same as the other Onshape assignments so far this year - you get a few concept sketches, and use them to create your own sketches in Onshape. However, here, it is slightly more challenging as there are several parts, hence the name "Multi Part Design Practice."

### Evidence
<img src="https://github.com/Raffi-Chen/engr3/assets/143544930/073d5c05-a951-4b63-b7b8-e7cd914a4c23" height="800"><br>
This shows everything that is necessary for the symmetric nature of this sketch.<br>

### Part Link 
[Link to part document](https://cvilleschools.onshape.com/documents/6b327a7fb8f7e4e606ec952c/w/5c49851c2f817853adb06a8c/e/175822094156ab05b063f33c).

### Reflection
I always say everything is "hard" on my reflections, and for a good reason. Each Engineering assignment isn't designed as busywork to give you work, but rather as something to help you grow on one new aspect. And this assignment is no different: the multi-part aspect really gave me something to work on. Well, honestly, it looked much more impressive than it actually was difficult, but its symmetric nature really intimidated me because of all the parts. The design intent included a full assembly on all of the parts, but all it did was boggle my concept of the part even more as I couldn't understand how it related to the isometric view (even though it very much did). Also, the design intent was spread out over two pages to disperse the information and make it easier to read, confusing me even more. The fact that the first question's pdf was 10 pages long also astonished me. However, I decided to simply force myself to work through it, hoping it would make sense later.

I started at the bottom cap (even though the first denoted item was the top cap), and while the specific parts themselves were only moderately difficult, the assembly all together was confusing. For example, when I started to calculate the masses of each parts, then I realized that I didn't interconnect all of the parts. When dimensions have parentheses around them, it means that they are taken from a reference and not from the actual dimension tool. I neglected this idea and started to get strange looks when changing dimensions for the other question. Then, I spent an extremely long time adjusting it (honestly doing it right the first time has its perks, especially with the time constraints). After all this, I still had some mistakes, realizing that I accidentally mistyped some of the dimensions. This lead me to realize the importance of double checking work, so that you don't do something slightly wrong. After all, just like in math, the end product (in this case the math) is what you need to get the question right, not the work. Another thing that influenced the mass, which I had to go back and fix, was their devious changing of materials at the bottom right on question 4. This shows the importance of looking at the specific aspects of the diagrams, even if they seem small and insignificant.





## VBlock

### Assignment Description
All of the Onshape Certification Prep assignments are essentially have the same, as the process in all of them is to follow a diagram and copy them to result in a final product that is based off of the picture. This one is another single part, which takes much shorter than the multipart designs.

### Evidence
<img src="https://github.com/Raffi-Chen/engr3/assets/143544930/25694afd-c356-4684-b010-b3834a1b7f94" height="800"><br>
Isometric view of part<br>
<img src="https://github.com/Raffi-Chen/engr3/assets/143544930/ca49ab1c-ada1-4589-b7dc-c0d28ab1843a" height="400"><br>
Left/right view of part showing hole at bottom of block and depths of extrudes<br>

### Part Link 
<a href="https://cvilleschools.onshape.com/documents/2b59c857ec3c50dd56544ca0/w/0fc1db2b5e7b3144fddd3604/e/2d713f247c81db7b9c473bec">Link to part document</a>

### Reflection
This one was a lot easier than the past multipart assignment, partially because it was intended to be done in half the amount of time. However, the schematic of this one was much easier to comprehend, as it didn't show a full assembly in one picture. This led to the feeling of the content being much less overwhelming, as since they only give you the essential information, you have to comprehend what is given but not emphasized. In this sketch, however, not much is emphasized, as there are only three sides to focus on rather than the 10 pages of the multipart cylinder assignment. Despite its ease, I did have a slight amount of problems with it. First of all, I did not know where to begin, and eventually started by literally drawing one side of the front with lines. This did work, however, I had to use the trick to adjust blue lines (by moving around the unconstrained points and finding where everything is) to eventually get to the schematic depicted on the diagram.

This is supposed to be completed in 30 minutes in the Onshape certification. So far, it is taking me around 50.





## AlignmentPlate

### Assignment Description
Same with the previous assignment, the purpose of this assignment is to create a single part based on a design schematic. This one is provided by the CAD Challenges extension.

### Evidence
<img src="https://github.com/Raffi-Chen/engr3/assets/143544930/261a6ade-389d-4145-b8ae-dea80ba85dc0" height="500"><br>
Isometric view of part<br>

### Part Link 
<a href="https://cvilleschools.onshape.com/documents/6531d2b5a342156cd69f113a/w/bdf0eeb5d408de85b6940585/e/6ea9ebaac577032a790e9f0a?renderMode=0&uiState=65528c6d6c67f86fd5900617">Link to part</a>

### Reflection
This piece was much easier than the other Onshape challenges so far, as it was a single part rather than a multi part. However, I did have some challenges on it despite its short time to complete. I initially thought that the part was symmetric, which it wasn't. However, only the ones that were consistent on both sides were symmetric, meaning the semicircles on both sides. However, the center oval is not symmetric, so you have to draw everything to be set to keep this in mind. This requires a lot more manual dimensioning, however, it is necessary for the awkward positioning of these parts.





## MicrophoneStand

### Assignment Description
This is another multipart assignment in which you simply follow the sketches in order to eventually achieve a certain result, in this case, a microphone stand (hence the name) which is modified through subsequent questions.

### Evidence
<img src="https://github.com/Raffi-Chen/engr3/assets/143544930/b39da8e0-ef14-4278-8cd4-80cd8a445347" height="600"><br>
Isometric view of part<br>
<img src="https://github.com/Raffi-Chen/engr3/assets/143544930/954c5c33-7bc0-488c-8717-da05116c5e0c" height="300"><br>
View with screw<br>
<img src="https://github.com/Raffi-Chen/engr3/assets/143544930/0b8317ff-8d88-4a76-a71c-c8cef708a2ad" height="500"><br>
Assembly view without post<br>

### Part Link 
<a href="https://cvilleschools.onshape.com/documents/291885c192991e3b50067efb/w/3dcd205d4c420829ad15136b/e/f6fed6615f5cb21381b85fdf?renderMode=0&uiState=65664252ed8d49509e55fdf7">Link to part document</a>

### Reflection
In this piece, I had a few problems about mass. I wanted to be exact to the options provided so I could be completely sure I did it correctly, and my results were more than the tenths place off. For the base, for example, I did not initally cut out the hole at the bottom enough, significantly adding to the mass here. After changing it to 3 mm, the mass matched perfectly. Another part that needed improvement was the fillets in the middle of the mic holder, as I needed them to be parallel and line up. Since we wanted them to be 3 mm apart throughout, then I found that one circle was filleted 7 mm and one 10 mm to make up for the discrepancy of distance.

One way I improved from previous assignments was to know to look carefully at parts and how they changed, which was extremely important on step 9, a question relying fully on part changes.





## Pliers

### Assignment Description
The purpose of this assignment is to follow the sketches and utilize the parts given in order to create an interconnected assembly with the parts and answer questions about this assembly.

### Evidence
![Assembly 1 (4)](https://github.com/Raffi-Chen/engr3/assets/143544930/98441b2b-0d72-47a7-8257-89e0b4e7eb2f)<br>
Isometric view of assembly<br>
![Assembly 1 (5)](https://github.com/Raffi-Chen/engr3/assets/143544930/54368bae-166e-4d2d-95a0-cdfbb9f49a4d)<br>
Same part, adjusted angles<br>

### Part Link 
<a href="https://cvilleschools.onshape.com/documents/6620e2e311f893dace40c32e/w/0d7cadc967ec9c42ab1f9413/e/778dca4b37ed80e49ca6bb6d?renderMode=0&uiState=659466c1ba37b256d8964c45">Link to part document</a>

### Reflection
Initially, I was confused how to connect the parts in order to make them work together (i.e. whether to use the revolute or fastened mate). Eventually, I realized that it was necessary to read between the lines in order for circular parts to rotate (revolute mate) and straight parts to stay fixed (fastened mate). Additionally, I did not initially know how to solve the questions where the angles were adjusted. I then realized that particular assembly features, like fastened mate, parallel, and distance, could be used for coincident, parallel, and offset, respectively.





## RotaryEncoder

### Description & Code Snippets
For this assignment, a rotary encoder was to be in control of an LCD screen, alternating between "Stop," "Caution," and "Go" and projecting each color (corresponding to the traffic light) onto the Metro's neopixel by pressing the button of the rotary encoder. I used a slide deck prepared by Ms. Gibson and Mr. Miller's help, as well as my previous documentation in order to complete this assignment.

In this assignment, I learned many skills to use a rotary encoder and LCD screen in CircuitPython.

```python

menu_index = 0

while True:

    menu_index = enc.position # Menu index is what encoder reads
    menu_index_lcd = menu_index % 3 # Finds remainder of # to read only 1, 2, or 3

    lcd.set_cursor_pos(0,0)
    lcd.print(menu[menu_index_lcd]) # Initiates + displays LCD values "stop", "caution", "go"

    if button.value and button_state == 0:

        if menu_index_lcd is 0:

            led[0] = (255, 0, 0)

    elif not button.value:

        button_state = 0 # Button is not pressed if not pressed
```

If you want to see the full code, it can be found <a href="https://github.com/Raffi-Chen/engr3/blob/main/Rotary%20Encoder.py">here</a>
 
### Evidence
https://github.com/Raffi-Chen/engr3/assets/143544930/6132dc27-5cf3-4f94-8170-3083129aa93c

### Wiring
![WIN_20240129_15_19_19_Pro](https://github.com/Raffi-Chen/engr3/assets/143544930/0a5ff063-6a89-4fd5-b756-c6300623cc45)
The large board depicted represents the microcontroller.

### Reflection
This assignment was particularly frustrating, as it was the first assignment in a long time featuring my fragmentary CircuitPython knowledge. Initially, I didn't even read the end goal / description of the assignment, going thorough the slide deck blindly and only hoping to get it finished. At this point, I wired all of my pieces based on my old documentation, which was a useful step even if I didn't realize it. 

I inserted much of the code from the slides, but lots of it turned out to be slightly faulty or up to interpretation. For example, I didn't realize that the LCD backpack scan code was used to find what library the LCD is used for, and instead was trying to use it to activate the LCD. This could be done by paraphrasing LCD code give further on the slide, as well as using code libraries to find basic LCD commands. The button's code was mostly given in the slide, and the rotary encoder code was partly given on the slide. However, I also had to ask Mr. Miller for help to get to my final goal. After writing this reflection, I'm realizing that I should use other people's documentation and reflections to aid my own Engineering knowledge - it's written to teach someone else, after all.





## Photointerrupters

### Description & Code Snippets
In this assignment, an LCD screen must keep track of how many times a photointerrupter is blocked. The code for this assignment is scaffolded off Ms. Gibson's pseudocode, and the wiring can be borrowed from previous documentation if necessary.

```python

while True:
    if (now + 4) < time.monotonic(): # If 4 seconds elapses

        lcd.set_cursor_pos(0,0) # Repeats line 18-21 with updated interrupt_counter value
        lcd.print("Interrupt Count:")
        lcd.set_cursor_pos(1,0)
        lcd.print(str(interrupt_counter))

    if photointerrupter.value == True:
        if photointerrupter_state == 0: # If photointerrupter interrupted, set photointerrupter_state to "interrupted"

            photointerrupter_state = 1
            interrupt_counter = interrupt_counter + 1 # adds to interrupt count by 1 if photointerrupter was previusly 0
    
    else:
        photointerrupter_state = 0 # if not covered, photointerrupter_state goes back to 0
```

The link to the full code can be found <a href="https://github.com/Raffi-Chen/engr3/blob/main/Photointerrupters.py">here</a>

### Evidence
https://github.com/Raffi-Chen/engr3/assets/143544930/7fa9ba40-dffd-4fbe-a613-b1282f53e3ce

### Wiring
![Powerful Trug](https://github.com/Raffi-Chen/engr3/assets/143544930/6a9ce5f3-53b9-41b7-aceb-baaec7dbbc5c)
For the wiring diagrams, I used <a href="tinkercad.com">TinkerCAD</a>. 
Substitutions: I used an Arduino Uno for my Metro M4, and a slideswitch instead of a photointerrupter.

### Reflection
This assignment is much more straightforward than the previous assignment, as the pseudocode is given. I also had the LCD from the previous assignment, further simplifying things. However, when I got into the nuts and bolts of the code, I did run into some actual problems. I was particularly confused by the arrangement of loops, as well as the meaning of time.monotonic. Apparently, the statement if (now + 4) < time.monotonic(): simply represented, in plain english, "if time is 4 more than I think time is, then update the program." My problem about the loops was offsetted by creating two if{ loops: one with all the information concerning the photointerrupters, and one concerning everything else. Additionally, I had a problem where the photointerrupter was constantly shooting 1s (reading something). I eliminated this repetition of readings by improving the photointerrupter loop. Essentially, the improved version states, in plain english, "if the photointerrupter was blocked and was not before, read once and then set to 'not read' if taken off".





## StepperMotors

### Description & Code Snippets
The goal of this assignment is to use a stepper motor to be able to continuously loop, using a limit switch to make it turn 180 degrees. To achieve this, the code tutorials from Ms. Gibson's code can be utilized

This function was new to me because it involved async, which I didn't fully understand until doing this assignment. It also involved controlling both a stepper motor and a limit switch to make the assignment function.

```python
from adafruit_motor import stepper # imports stepper motor

DELAY = 0.01
STEPS = 100

motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)
 
async def catch_pin_transitions(pin): # Loop 1 responds to limit switch when pressed
    with keypad.Keys((pin,), value_when_pressed=False) as keys:
        while True:
            event = keys.events.get()
            if event:
                if event.pressed:
                    print("Limit Switch was pressed.")
                    for step in range(STEPS):
                        motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE) # Tells stepper motor to move backwards
                        time.sleep(DELAY)
```

Link to code: <a href="https://github.com/Raffi-Chen/engr3/blob/main/StepperMotors.py">https://github.com/Raffi-Chen/engr3/blob/main/StepperMotors.py</a>

### Evidence
https://github.com/Raffi-Chen/engr3/assets/143544930/006c3546-710a-4c78-b5bb-10644ff9ff5e

### Wiring
![WIN_20240226_15_35_47_Pro](https://github.com/Raffi-Chen/engr3/assets/143544930/9c6f6295-5e8a-4131-9526-36267d246c53)

### Reflection
At first, I simply started with Ms. Gibson's tutorial to get a general feel for the project. This worked for all of the parts and turned out easier than I expected at first. However, my major difficulty with this assignment was the code, when I tried to start putting everything together. Eventually, Mr. Miller helped me realize that the async def functions helped run multiple things at the same time, through a pseudo-simultaneous sequence of flashing between many loops at the same time. These loops were the constant running of the motor, the press and release to shift direction, and one to run the asyncio and do both functions at the same time. After working through these two simple commands, the assignmment was, for the most part, complete, reminding me that I should remember to break work down in chunks rather than finishing it quickly all at one time.





## IRSensors

### Description & Code Snippets
This assignment was used to learn how to use IR sensors, and it simply needed to turn the board's neopixel green when not blocked, and red when blocked. Ms. Gibson's tutorial essentially had everything except for the basics, helping to master the basics of CircuitPython.

In terms of code, I learned how to initiate and use an IR sensor as well as reviewing the use of the neopixel.

```python
import neopixel
import digitalio

# Set up the IR Sensor using digital pin 2.
ir_sensor = digitalio.DigitalInOut(board.D2)

# Set the photointerrupter as an input.
ir_sensor.direction = digitalio.Direction.INPUT 

# While loop runs the code inside continuously.
while True:
    # If an object is near the IR sensor (sensor is LOW):
    if ir_sensor.value is False:
        # Set Neopixel color to RED
        led[0] = (255,0,0)
```
You can find the full code here: <a href="https://github.com/Raffi-Chen/engr3/blob/main/IR%20Sensors.py">https://github.com/Raffi-Chen/engr3/blob/main/IR%20Sensors.py</a>

### Evidence
https://github.com/Raffi-Chen/engr3/assets/143544930/39905ffe-0d60-4a67-bbbd-3a92b38d9e62

### Wiring
![gewagewagewagewgwa](https://github.com/Raffi-Chen/engr3/assets/143544930/50c13541-1221-451a-acba-2f13ed98ad03)
For my wiring diagram, I used [tinkercad.com](https://www.tinkercad.com/learn/circuits). I substututed the Metro M4 for an Uno.

### Reflection
This assignment was much easier than I expected, as it was mostly application from previous CircuitPython assignments, which I am becoming more and more familiar with. Additionally, it was relatively simple, especially the wiring, which only involved one component. One of my struggles was that I was still in "arduino mode" in terms of code, almost making up code in some sections because I didn't know the precise notation for each section. For example, on line 21, I wrote ir_sensor is LOW, forgetting that it needed to be a .value to represent a 0 or a 1, and I also wrote LOW instead of False, which is the correct notation for 0/1 (True/False). I also put an equals sign after my print statements. Although these errors were relatively close to the actual fix, they showed how much precision was necessary for code. However, with the right dedication, the fix is always right around the corner - it's simply a matter of pinpointing what to fix!





## RobotGripper

### Assignment Description
This is intended as preparation for the Robot Arm project, so that I can have a base idea of how my robot arm will function before a more complex project involving this arm. In order to create the robot arm, it should be sketched with basic emulations of realistic, intended dimensions as well as holes to attach nuts and bolts. It should be able to fully close and come with an assembly and simulation.

### Evidence
![Assembly 1 (6)](https://github.com/Raffi-Chen/engr3/assets/143544930/397c0cd1-80dc-48e8-8306-af38ecd5a894) Isometric view of arm
![Assembly 1 (7)](https://github.com/Raffi-Chen/engr3/assets/143544930/99322919-3446-4d65-977a-9131b8b6b7cc) Opened arm from front view
![Assembly 1 (8)](https://github.com/Raffi-Chen/engr3/assets/143544930/875709a0-f562-4d11-abd0-b9b22693dc40) Closed arm from back view<br>
![trshstrhttrhrssttrtterrydfg vfhg](https://github.com/Raffi-Chen/engr3/assets/143544930/2a96d7f8-4cd4-4a92-b5ac-530073c2263d) <br>Bill of Materials



### Part Link 
<a href="https://cvilleschools.onshape.com/documents/057796055cd2d7638fe1e160/w/7c6c6bc64f761cb42595d24e/e/bbb8696a64a2ab37d9ef15bf?renderMode=0&uiState=65e8c7c8b6ae8632511f6997">Link to part document</a>

### Reflection
I used the bare minimum of my current Onshape knowledge to tread through this assignment. This worked for the most part, however, I ran into a few walls that had quick solutions. After creating an arm that encapsulated the general idea of the robot, I ran into the problem of setting the limits to be accurate to the opening of the robot. The solution to this was quite simple - I simply needed to check the slider mate and hit "limits". However, afterwards, I ran into some problems with the mating (to find accurate limits). To solve this, I played around with where the mates were fastened or planar, and where they were placed. (This is definitely something I'm still working on). I also did more work than I needed to with the standard content initially, but later realized that I could use the Replicate feature to do one thing in many different instances.



<!--

ARDUINO
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





ONSHAPE
## Onshape_Assignment_Template

### Assignment Description
Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence
Take several cropped screenshots of your Onshape document from different angles. Try to capture all important aspects of the design. Turn off overlays that obscure the parts, such as planes or mate connectors. Your images should have captions, so the reader knows what they are looking at!  

### Part Link 
[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

-->

<!--References for commonly used sources-->
<!--For the wiring diagrams, I use <a href="tinkercad.com">TinkerCAD</a>.-->
