#!/usr/bin/env python3
import base64

def encrypt(plain,key):
    result = ""
    for i in range(len(plain)):
        result += chr(plain[i] ^ key[i%len(key)])
    
    # diencode ke base64 biar gampang dibaca
    return base64.b64encode(result.encode())

plain = b"HALLO"
key = b"Rahasia dong :)" # bukan ini keynya, silahkan tebak h3h3
cipher = encrypt(plain,key)
print(base64.b64decode(cipher))
print(base64.b64decode(encrypt(base64.b64decode(cipher),key)))

# with open("flag.enc","wb") as f:
#     f.write(cipher)