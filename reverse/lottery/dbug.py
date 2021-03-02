from random import randint
ticket = "H673uv0Z2o2wR5mimiaO64c0yZ0Or8r7mY3z16024faLazxT80"
prob = 17
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
notPrime = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 
            24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39,
            40,42, 44, 45, 46, 48, 49]

moduleFive = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
moduleNine = [0, 9, 18, 27, 36, 45]
moduleThirteen = [0, 13, 26, 39]
moduleFour = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]
moduleThree = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33,
                36, 39, 42, 45, 48]

# 48 <= ord(ticket[i]) ^ i % 10 <= 57
valid1 = [2,3,13,23,29,31,37]
# 65 <= ord(ticket[i]) - 20 <= 90
valid2 = [14, 15, 16, 18, 22, 25, 32, 33, 42, 44]
a = 0
for i in range(50):
    a = i%10
    print(a)