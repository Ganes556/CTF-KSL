from Crypto.Util.number import inverse
c = [54936, 44165, 43788, 47332, 23993, 26956, 27917, 26956, 54434, 29636, 39354, 29477, 27917, 29636, 12626, 27917, 29477, 29636, 9331, 27917, 29477, 54434, 29636, 9331, 22640, 45837, 33284, 19382, 41280, 39004, 39004, 39004, 31084]
n = 55189
e = 7

p = 229
q = 241
phi = (p - 1) * (q - 1)
d = inverse(e,phi)

for i in c:
    print(chr(pow(i,d,n)),end="")
