import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 25, 8, 7, 12, 16, 20, 21]
aux = [2, 3, 14, 15, 18, 27, 23, 22]

GPIO.setup(aux, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 1)

a_l = {2:24, 3:25, 14:8, 15:7, 18:12, 27:16, 23:20, 22:21}



while True:
    for i in aux:
        print(GPIO.input(i))
        if GPIO.input(i) == 0:
            GPIO.output(a_l[i], 0)
        else:
            GPIO.output(a_l[i], 1)