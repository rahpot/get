import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
leds = [24, 25, 8, 7, 12, 16, 20, 21]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

def t_t(value):
    return [int(bit) for bit in bin(int(value))[2:].zfill(8)]
    
def adc():
    n = [0 for i in range(8)]
    for i in range(8):
        n_n = n.copy()
        n_n[i] = 1
        GPIO.output(dac, n_n)
        time.sleep(0.005)
        if GPIO.input(comp) == 1:
            n = n_n
    r = ''.join([str(i) for i in n])
    return int(r, 2)

try:
    while True:
        n = adc()
        print ("предполагаемое напряжение: {0:.2f}В".format(int(n)/255 * 3.3))
        kol = int(n)/255 * 3.3
        kol = kol / 3.28
        kol = kol * 8
        kol = round(kol)
        print(kol)
        GPIO.output(leds, 0)
        for i in range(kol):
            GPIO.output(leds[i], 1)
            
        
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()


