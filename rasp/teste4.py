import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

vazamento = 0

try:
    while True:
        if GPIO.input(4):
            print("Sem Vazamento")
            print(GPIO.input(4))
        else:
            print("Tá Vazando")
            print(GPIO.input(4))
            vazamento += 1
        
        sleep(1)

        if vazamento > 4:
            print("Enviando dados para o servidor")
            sleep(10)

finally:
    print("Termina")
    GPIO.cleanup()
