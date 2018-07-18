import requests

r = requests.post("http://10.42.0.1:5000/login/kz912/seecret")
#this logs the user in, replace kz912 with a netID of your choice
#"seecret" is the password for the netID's "account," can be any combination of numbers/letters

print(r.text)