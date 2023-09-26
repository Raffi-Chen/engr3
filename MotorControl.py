import board
import time
import analogio
import pwmio

pot = analogio.AnalogIn(board.A1) # initialize analog input for potentiometer
motor = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=5000) # use pwm output to pin 3 for motor

while True:
    try:
        print(pot.value)
        motor.duty_cycle=(pot.value) # set motor to potentiometer input
        time.sleep(0.01)

    except RuntimeError:
        print("Retrying!")
        time.sleep(0.1)