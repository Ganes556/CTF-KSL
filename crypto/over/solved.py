import os
from base64 import *
def decode(encFlag,encSendiri,plainSendiri):
    key = getkey(encSendiri,plainSendiri)
    decoded = ''
    for i in range(len(encFlag)):
        # simpler = ~(encFlag[i]) & key[i%len(key)] | encFlag[i] & ~(key[i%len(key)])   --> penyederhanaan dari codenya
        plain = encFlag[i] ^ key[i%len(key)] # ternyata sama dengan ini 
        decoded += chr(plain)
    print(decoded)

def getkey(enc,plain):
    key = b""
    for i in range(len(enc)):
        key += chr(enc[i]^ord(plain[i])).encode("latin1")
    return key
    
enc = b64decode("958ahUG353cgC46Meda+5etI/MCXtwuTSGG84nOZtbC2+NR+FbA=")
encSendiri = b64decode("xbg8pX6ex10SLJGfWJeppfdfuOOulVqnFkaFyyi955CH+II+Hq4CD8i9GqKDjGqQmB5+lHn3K8JbmpvC5W5JdxD/ZlmytFsDHKYkSQ==")
decode(enc,encSendiri,"asokpdfoasdfopasndpofnasodfnopasndfpociasndfopiasnodpfinasoipfnasopifnosapnf")