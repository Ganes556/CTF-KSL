#!/usr/bin/env python3
from base64 import *
import os

KEY = os.urandom(256)

def enc(data):
    key = KEY[:len(data)]
    cipher = ''
    for i in range(len(data)):
        p1 = ~(ord(data[i]) & key[i%len(key)])
        p2 = ~(ord(data[i]) & p1)
        p3 = ~(key[i%len(key)] & p1)
        p4 = ~(p2 & p3)
        cipher += chr(p4)
    
    cipher = b64encode(cipher.encode("latin1")).decode("ascii")
    print(key)
    return cipher
 

def main():
    print("Overcomplicated encryption...")
    print("[1] Get secret message")
    print("[2] Encrypt your own message")
    print("[3] Exit")
    inp = input("Input: ")
    if inp == "1":
        flag = open("flag.txt","r").read().strip()
        print("Secret message:",enc(flag),end="\n\n")
    elif inp == "2":
        msg = input("Input your message:\n")
        print("Encrypted message:",enc(msg),end="\n\n")
    elif inp == "3":
        print("Goodbye...")
        exit()
    else:
        print("Invalid input...",end="\n\n")
# flag --> fy+nMnwVDEQ1VhHSFg7f1Tmz10vhoENpiZUkgjkcQohqPNom290=
if __name__ == "__main__":
    while True:
        main()
    