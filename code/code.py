import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

lr = digitalio.DigitalInOut(board.A5)
lr.direction = digitalio.Direction.INPUT


i0 = digitalio.DigitalInOut(board.D5)
i0.direction = digitalio.Direction.INPUT

i1 = digitalio.DigitalInOut(board.D6)
i1.direction = digitalio.Direction.INPUT

i2 = digitalio.DigitalInOut(board.D9)
i2.direction = digitalio.Direction.INPUT

i3 = digitalio.DigitalInOut(board.D10)
i3.direction = digitalio.Direction.INPUT



while True:
    #print("button: {}".format(lr.value))
    print("i0: {} i1: {} i2: {} i3 {}".format(int(i0.value), int(i1.value), int(i2.value), int(i3.value)))
    # print(lr.value)
    time.sleep(0.001)


# runs = 0
# while True:

#     led.value = True
#     time.sleep(0.000000001)
#     led.value = False
#     time.sleep(0.000000001)

#     # print(runs)
#     # runs += 1
#     if(lr.value):
#         print("HIGH")
#     else:
#         print("LOW")
