#!/usr/bin/env python3
from Crypto.Util.number import *

while True:
    p = getPrime(1024)
    q = getPrime(1024)
    r = getPrime(1024)
    n1 = p*q
    n2 = q*r
    phi1 = (p-1)*(q-1)
    phi2 = (q-1)*(r-1)
    e = 65535

    if GCD(e,phi1) == 1 and GCD(e,phi2) == 1:
        break
    # flag = open("flag.txt","rb").read()
    # m = bytes_to_long(flag)
m1 = inverse(e,phi1)
m2 = inverse(e,phi2)
c1 = pow(m1,e,n1)
c2 = pow(m2,e,n2)

print("n:",n1)
print("c:",c1)
print()
print("n:",n2)
print("c:",c2)

del p,q,r,phi1,phi2

#anehman@pramayasa:~$ python3 rsa.py > result.txt