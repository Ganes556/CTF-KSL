import requests
url= "http://103.145.226.170:3000/"
a = {
   "User-Agent": "KSL_BROWSER", 
    }

print(requests.get(url,headers=a).text)