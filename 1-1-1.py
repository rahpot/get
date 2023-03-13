import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
    
names = [21, 20, 16, 12, 7, 8, 25, 24]
while True:
    for i, zn in enumerate(names):
        GPIO.output(names[i-1], 0)
        GPIO.output(zn, 1)
        time.sleep(0.1)
    
