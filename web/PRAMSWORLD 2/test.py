import requests
url = "http://103.145.226.170:2000/"
my_file = {"File" : open('index.php','r')}
r = requests.post(url,file=my_file)
print(r.text)