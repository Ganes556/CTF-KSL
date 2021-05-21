from PIL import Image

im = Image.open("ubuntu.png")
im2 = Image.open("ubuntu_embedded.png")

a = im.getdata() # ambil semua data pixel ori
b = im2.getdata() # ambil semua data pixel embed


isinya = [x for i in a for x in i] # ori
isinya2 = [y for j in b for y in j] # embded
double = zip(isinya,isinya2)
# 1. bandingkan pixelnya, nah karna di troublemaker itu bilang bahwa messagenya di jadiin biner
# 2. trus pixel si ori dikurangi dengan 1 dan 0
# 3. jadi ya saya tinggal bandingin pixel nya jika pixel orinya tidak sama dengan yang embed 
    # jadinya itu hasil dari pengurangan 1 pada biner
# 4. trus jika pixel orinya sama dengan yang embed 
    # jadinya itu hasil dari pengurangan 0 pada biner atau sudah habis messagenya atau panjang flagnya sudah habis 

### dapatkan binernya 
binerT = ""
for ori,embed in double:
    if ori != embed:
        binerT +="1"
    if ori == embed:
        binerT +="0"
### lalu convert binernya ke string
mes = ""
flag = ""
for n in binerT:
    mes +=n
    if len(mes)%8 == 0:
        # print(mes)
        flag += chr(int(mes,2))
        mes = ""
open("flag.txt","w").write(flag)