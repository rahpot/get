import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)

def t_t(value):
    return [int(bit) for bit in bin(int(value))[2:].zfill(8)]
    
def adc():
    for i in range(256):
        GPIO.output(dac, t_t(i))
        time.sleep(0.0005)
        if GPIO.input(comp) == 0:
            return i
    return 0

try:
    while True:
        n = adc()
        print ("предполагаемое напряжение: {0:.2f}В".format(int(n)/255 * 3.3))
        GPIO.output(dac, t_t(n))
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
