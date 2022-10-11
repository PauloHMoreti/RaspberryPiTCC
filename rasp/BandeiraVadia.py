import requests
import json

server = "http://localhost:38000/device"

gets = json.loads(requests.get(server).text)

for get in gets:
    for item in get:
        print(item, get[item])
    print()

pload = {'name':' viado','email':'primianoviado@homosexual.cum', 'password':'sim123', 'phoneNumber':'198823', 'cpf':'69420'}
r = requests.post(server,json = pload)
print(r.text
import requests
import json

server = "http://localhost:38000/device"

gets = json.loads(requests.get(server).text)

for get in gets:
    for item in get:
        print(item, get[item])
    print()

pload = {'name':' viado','email':'primianoviado@homosexual.cum', 'password':'sim123', 'phoneNumber':'198823', 'cpf':'69420'}
r = requests.post(server,json = pload)
print(r.text)
