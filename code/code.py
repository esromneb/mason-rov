import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

lr = digitalio.DigitalInOut(board.D10)
lr.direction = digitalio.Direction.INPUT

runs = 0
while True:
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.1)
    # print(runs)
    # runs += 1
    if(lr.value):
        print("HIGH")
    else:
        print("LOW")

