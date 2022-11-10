import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.IN)

try:
    while True:
        if GPIO.input(4):
            print("Vazando")
            print(GPIO.input(4))
            print(GPIO.input(17))
        else:
            print("Safe")
            print(GPIO.input(4))
            print(GPIO.input(17))
        sleep(1)

finally:
    print("Termina")
    GPIO.cleanup()

