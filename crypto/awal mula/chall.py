#!/usr/bin/env python3
import base64

def encrypt(plain,key):
    result = ""
    
    for i in range(len(plain)):
        # result += chr(ord(plain[i]) ^ key[i%len(key)])
        result += chr(plain[i] ^ key[i%len(key)])
        # print(key[i%len(key)])
    # diencode ke base64 biar gampang dibaca
    return result
    # return base64.b64encode(result.encode())
plain = b"HALLO"

# plain = open("flag.txt","rb").read()
key = b"Rahasia dong :)" 
encr = encrypt(plain,key).encode()
print(encr)
print(encrypt(encr,key))

# def decrypt(plain,key):
#     result = ""
#     for i in range(len(plain)):
#         result += chr((plain[i] ^ key[i%len(key)]) ^ plain[i])
    
#     # diencode ke base64 biar gampang dibaca
#     return result
# plain = base64.b64decode("IzIgXW9fURYWXQcLUQFcABlRMgxeD1sTAjAcHxgdFV4MGlUcBwYyA10SPx4NHA==".encode())
# key = base64.b64decode("LAAADjJNCh8IHh8HBh4OOQRNTTkhOUgSCQs6HwkMDw9LCgQeAC8IEwwSB0sbBA4OOAwITQMLGQEKGRtVZyBNP04pSFxMLFUsQTNBLUtVQS5lHU0/TSJOVkggZmUbBAMMFg8DSAAIDn8EDB0NCwYNDxgOLARBNS48SwUEAgg4GA8MCg8FSBEVGzcCD0NBLAIbAEwEPgVBBgACAgkPTAs+HQQZCABLDg0NCDEUAFJeZA==".encode())
# print(decrypt(plain,key))



# plain = b"hello"
# key = b"test"
# print(encrypt(plain,key))
# cipher = encrypt(plain,key)

# with open("flag.enc","wb") as f:
#     f.write(cipher)