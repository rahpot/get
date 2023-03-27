import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
pwm22 = GPIO.PWM(22, 500)

try:
    dc = float(input("Введите коэффициент заполнения: "))
    pwm22.start(dc)
    while True:
        GPIO.output(21, GPIO.input(22))
finally:
    GPIO.cleanup()
