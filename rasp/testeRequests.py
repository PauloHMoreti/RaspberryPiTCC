import requests
from getmac import get_mac_address as gma

a = requests.get("https://gsense.azurewebsites.net/GSense-0.0.1-SNAPSHOT/device/test/1/1")
print(gma())
print(a)


#idDevice: 1
#deviceNumber: 1
#Vazamento: 