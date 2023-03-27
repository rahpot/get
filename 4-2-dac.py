import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(value):
    return [int(bit) for bit in bin(int(value))[2:].zfill(8)]


try:
    t = int(input("введите желаемый период: "))
    s = 0
    v = 1
    while True:
        if s >= 256:
            v = -1
            s = 255
        elif s <= -1:
            v = 1
            s = 0
        GPIO.output(dac, dec2bin(s))
        time.sleep(t/512)
        s += v
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()