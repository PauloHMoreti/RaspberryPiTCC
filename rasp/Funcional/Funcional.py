#Importando as bibliotecas:
import RPi.GPIO as GPIO
from time import sleep
import requests
from getmac import get_mac_address as deviceNumber

#Configurações Gerais:
portaSensor = 4
vazamento = 0

#Configurações do GPIO:
GPIO.setmode(GPIO.BCM)
GPIO.setup(portaSensor, GPIO.IN)
sensor = GPIO.input(portaSensor)

#Codigo Principal:
try:
    while True:
        if sensor:
            print("Sem Vazamento")
            print(sensor)
        else:
            print("Tá Vazando")
            print(sensor)
            vazamento += 1
        
        sleep(1)

        if vazamento > 4:
            print("Enviando dados para o servidor")
            sleep(10)

finally:
    print("Termina")
    GPIO.cleanup()
