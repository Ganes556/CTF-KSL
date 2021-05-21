#!/usr/bin/env python3
from Crypto.Cipher import AES
import os

def encrypt(msg):
    IV = b'\x00'*16
    aes = AES.new(KEY,AES.MODE_CFB,IV)
    enc = aes.encrypt(msg)
    return enc

def input_check(inp,secret):
    if inp == secret:
        print("AMJER DUKUN")
        os.system("cat flag.txt")
        exit()
    else:
        print("SALAH KAWOKAWOAKWOAKW\n")

if __name__ == "__main__":
    print("Met datang ea....")
    print("Kalo bisa bikin input == encrypt(input), dapet flag h3h3")
    while True:
        KEY = os.urandom(16)
        
        inp = input("Input: ").encode()

        if len(inp) < 8:
            print("MINIMAL 8 KARAKTER WOY!!!!1!1!1!satu!!\n")
            continue

        e = encrypt(inp)

        input_check(inp,e)