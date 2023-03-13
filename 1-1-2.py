import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)
GPIO.setup(14, GPIO.OUT)

while True:
    print(GPIO.input(2))
    GPIO.output(14, GPIO.input(2))
