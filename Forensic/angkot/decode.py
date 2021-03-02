from PIL import Image

im = Image.open('ubuntu.png', 'r')
data = im.getdata()

im2 = Image.open('ubuntu_embedded.png','r')
data2 = im2.getdata()

isi = [x for i in data for x in i]
isi2 = [y for i in data for y in i]

double = zip(isi,isi2)
i = 1
x = ""
for a,b in double:
    x+= str((a-b)%256)
    if i == 1000:
        break
    i+=1

print(x)



# isinya = [x for i in data for x in i]
# text = ''
# for i in isinya:
#     text += chr(i)
# print(text)
# print(text.replace("ÿ",""))
