import requests
import nmap
data = {"username":"KSL","password":"BROWSER"}
r = requests.post("http://103.145.226.170:3000/",data=data)
print(r.text)