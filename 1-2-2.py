import RPi.GPIO as GPIO
import time
import random as rd


dac = [10, 9, 11, 5, 6, 13, 19, 26]
number = [0 for i in range(8)]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
number1 = [0, 1, 0, 0, 0, 0, 0, 0]
number2 = [1, 1, 1, 1, 1, 1, 1, 1]
number3 = [1, 1, 1, 1, 1, 1, 1, 0]
number4 = [0, 0, 0, 0, 0, 0, 1, 0]
number5 = [0, 0, 0, 0, 1, 0, 0, 0]
number6 = [1, 0, 1, 0, 0, 0, 0, 0]
number7 = [0, 0, 0, 0, 0, 0, 0, 0]
number8 = [1, 0, 0, 0, 0, 0, 0, 0]
n = [number4, number2, number3, number4, number5, number6, number7, number8] 
for i in n:
    GPIO.output(dac, i)
    time.sleep(10)
    GPIO.output(dac, 0)
GPIO.cleanup()


