import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

try:
    while True:
        if GPIO.input(4):
            print("Vazando")
            print(GPIO.value(4))
        else:
            print("Safe")
            print(GPIO.value(4))

        sleep(1)

finally:
    print("Termina")
    GPIO.cleanup()

