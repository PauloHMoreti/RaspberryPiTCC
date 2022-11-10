#Importando as bibliotecas
#import RPi.GPIO as GPIO
#from time import sleep
import requests
#import json

#Inciando a porta do GPIO:

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

#Variaveis Essenciais:

vazamento = 0
Sensor = GPIO.input(4)
Host = "http://10.9.1.6:38000/device"  #Colocar o IP e a porta do HOST - SEMPRE ENTRE ASPAS!!

print("Iniciado")

#Request:

print("teste")
pload = {'deviceNumber': '69', 'deviceId': '6'}
print("teste2")
r = requests.post(Host,data = pload)
print(pload)
print(r.text)


a = requests.get("http://10.9.1.6:38000/users")
print(a)

#Codigo principal:
try:
    while True:
        if Sensor:
            print("Sem Vazamento")
            print(Sensor)
            get.status_code
        else:
            print("Tá Vazando")
            print(Sensor)
            vazamento += 1
        
        sleep(1)

        if vazamento > 4:
            print("Enviando dados para o servidor")
            sleep(10)

finally:
    print("Termina")
    GPIO.cleanup()