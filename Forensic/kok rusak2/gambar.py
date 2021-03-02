from PIL import Image

import os
# img = Image.open("flag(1).png")

img = open("flag(1).png","rb")
hexData = ""
dataStr = ""
for i in img.read():
    hexData+= "".join(hex(i).strip("0x").upper())
    dataStr+= "".join(chr(i))


status = ["PNG","IHDR","IDAT","IEND"]
a = [True for i in status if i in dataStr]
if a == []:
    hexData = hexData.replace(hexData[:16],"89504E470D0A1A0A")
dataStr = 
print()


# os.system("pngcheck flag(1).png")

# print(dataStr.find("PHYZ"))
# print(dataStr[37:-1])

# datastr2 = ""
# for i in dataStr:
#     datastr2 += "".join(hex(ord(i)).strip("0x").upper())

# if hexData == datastr2:
#     print(True)



# size = w,h = img.size()

# data = img.load()

# for x in range(w):
    # for y in range(h):
        # print(y)