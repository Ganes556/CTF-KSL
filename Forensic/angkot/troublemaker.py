from PIL import Image

im = Image.open("ubuntu.png")
pix = im.load()

secret = open("secret.txt","rb").read().hex()
message = [secret[i:i+2] for i in range(0,len(secret),2)]

# hex jadiin biner dengan panjang 8 tiap karakternya
i = 0
for m in message:
    m = bin(int(m,16))[2:]
    while len(m) % 8 != 0:
        m = "0" + m
    message[i] = m
    i += 1

message = ''.join(message)
# dibagi 3 agar pas dengan array dari pixelnya
while len(message) % 3 != 0:
    message += "0"

message = [int(i) for i in message]

w = 0
for y in range(im.size[1]):
    for x in range(im.size[0]):
        if w == len(message):
            im.save("ubuntu_embedded.png")
            exit()
        embed = [message[w], message[w+1], message[w+2]]
        ori = list(pix[x,y])
        for i in range(3):
            ori[i] = (ori[i] - embed[i]) % 256
        pix[x,y] = tuple(ori)
        w += 3