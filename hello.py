# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
import digitalio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

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
    if pressed !=button_state:
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(0.05)
    else:
        if pressed !=button_state2:
            for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
                my_servo.angle = angle
                time.sleep(0.05)
            else: pass
    button_state = pressed