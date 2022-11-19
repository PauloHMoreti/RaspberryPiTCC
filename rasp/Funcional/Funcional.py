#Importando as bibliotecas:
import RPi.GPIO as GPIO
from time import sleep
import requests
from getmac import get_mac_address as MacAddress

#Configurações Gerais:
portaSensor = 4
vazamento = 0
deviceNumber = 19
host = "http://10.1.9.1:38000/device/dashboard"

#Configurações do GPIO:
GPIO.setmode(GPIO.BCM)
GPIO.setup(portaSensor, GPIO.IN)

#Iniciando o sistema:
firstPost = requests.post(host + f"/{deviceNumber}/0")
print(firstPost)

#Codigo Principal:
try:
    while True:
        if GPIO.input(portaSensor):
            print("Sem Vazamento")
            print(GPIO.input(portaSensor))
        else:
            print("Tá Vazando")
            print(GPIO.input(portaSensor))
            vazamento += 1
        
        sleep(1)

        if vazamento > 4:
            print("Enviando dados para o servidor")
            vazamentoPost1 = requests.post(host + f"/{deviceNumber}/1")
            print(vazamentoPost1)
            sleep(10)
            vazamento = 0
            vazamentoPost2 = requests.post(host + f"/{deviceNumber}/0")
            print(vazamentoPost2)
            
finally:
    print("Termina")
    GPIO.cleanup()
