from PIL import Image

im = Image.open('end_of_life.png', 'r')
data = im.getdata()
isinya = [x for i in data for x in i]
text = ''
for i in isinya:
    text += chr(i)
print(text.replace("ÿ",""))
