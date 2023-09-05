
# importing certian aspects to code
import time
import board # allow board to connect
import pwmio # pulse width modulation: allow servo to comm with board
import digitalio
from adafruit_motor import servo # imports servo

# initializes pulse width modulation and constraints concerning it on board
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# my_servo is initializes as servo variable
my_servo = servo.Servo(pwm)

# define pins for each button
pin = digitalio.DigitalInOut(board.D1)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP

button_state = False

pin2 = digitalio.DigitalInOut(board.D2)
pin2.direction = digitalio.Direction.INPUT
pin2.pull = digitalio.Pull.UP

button_state2 = False


while True:
    pressed = pin.value
    # if left button pressed
    if pin.value:
        print("Left")
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(0.05)
    # if right button pressed
    if pin2.value:
        print("Right")
        for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(0.05)
    button_state = pressed