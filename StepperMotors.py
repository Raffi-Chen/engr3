import asyncio # Initiates "fake" multi-threading in order to "do" multiple things at the same time
import board
import keypad # communicate with limit switch
import time
import digitalio # 
from adafruit_motor import stepper # imports stepper motor

DELAY = 0.01
STEPS = 100

coils = ( # Distributes stepper motor to multiple centers for power
    digitalio.DigitalInOut(board.D9),  # A1
    digitalio.DigitalInOut(board.D10), # A2
    digitalio.DigitalInOut(board.D11), # B1
    digitalio.DigitalInOut(board.D12), # B2
)

for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT

motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)
 
async def catch_pin_transitions(pin): # Loop 1 responds to limit switch when pressed
    # Print a message when pin goes low and when it goes high.
    with keypad.Keys((pin,), value_when_pressed=False) as keys:
        while True:
            event = keys.events.get()
            if event:
                if event.pressed:
                    print("Limit Switch was pressed.")
                    for step in range(STEPS):
                        motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE) # Tells stepper motor to move backwards
                        time.sleep(DELAY) 
                elif event.released: # when released
                    print("Limit Switch was released.")
            await asyncio.sleep(0) # Tell asyncio to go to the next event immediately

async def run_motor(): # Constant limit switch loop
    while(True):
        for step in range(STEPS):
            motor.onestep(style=stepper.DOUBLE)
            time.sleep(DELAY)
        await asyncio.sleep(0)

async def main(): # in this loop, both async functions are defined as new asyncio tasks
    while(True):
        interrupt_task = asyncio.create_task(catch_pin_transitions(board.D2))
        motor_task = asyncio.create_task(run_motor())

        await asyncio.gather(interrupt_task, motor_task)

asyncio.run(main()) # Finalizes asyncio run
