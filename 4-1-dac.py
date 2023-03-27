import RPi.GPIO as GPIO
dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def t_t(value):
    return [int(bit) for bit in bin(int(value))[2:].zfill(8)]
    

try:
    while True:
        n = input("введите число от 0 до 255: ")
        if n == 'q':
            break
        elif n.isalpha():
            print('Не числовое значение')
        elif int(float(n)) != float(n):
            print('Не целое число')
        elif float(n) < 0:
            print('Число меньше нуля')
        elif int(n) > 255:
            print('Превышающее значение')
        else:
            print ("предполагаемое напряжение: {0:.2f}В".format(int(n)/255 * 3.3))
            GPIO.output(dac, t_t(n))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
