import board
import neopixel
import digitalio

# Set up the IR Sensor using digital pin 2.
ir_sensor = digitalio.DigitalInOut(board.D2)

# Set the photointerrupter as an input.
ir_sensor.direction = digitalio.Direction.INPUT 
            
# Use the internal pull-up resistor.
ir_sensor.pull = digitalio.Pull.UP

# Initialize the on-board neopixel and set the brightness.
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.1

# While loop runs the code inside continuously.
while True:
    # If an object is near the IR sensor (sensor is LOW):
    if ir_sensor.value is False:
        # Print something to the Serial Monitor.
        print("blocked")
        # Set Neopixel color to RED
        led[0] = (255,0,0)

    # If nothing is near the IR sensor (sensor is HIGH):
    if ir_sensor.value is True:
        # Print something to the Serial Monitor.
        print("not blocked")
        # Set Neopixel color to GREEN
        led[0] = (0,255,0)
