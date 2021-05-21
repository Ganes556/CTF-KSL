serial_key = [0]*65
def validate(kode):
    global serial_key
    skor = 0
    
    if len(kode) != 65:
        print("salah")
        return

    p1 = kode[:16] # 0-15
    p2 = kode[17:32] # 17-31
    p3 = kode[33:48] # 33-47
    p4 = kode[49:] # 49-65
    
    collected_string = []

    for i in range(16):
        if 32 <= ord(p1[i]) <= 126:
            if p1[i] not in 'LMAO':
                if p1[i] not in ' ~`!@#$%^&*()_+=-}{][|"\'<,>.?/:;\\':
                    if p1[i] not in collected_string and p1[i] not in serial_key:
                        collected_string.append(p1[i])
                        if p1[i] not in 'abcdefghijklmnopqrstuvwxyz':
                            serial_key[i] = p1[i]
                            skor += 1
    
    if kode[16] == '-': # 16
        serial_key[16] = "-"
        skor += 1
    for i in range(15):
        if 32 <= ord(p2[i]) <= 126:
            if p2[i] not in collected_string and p2[i] not in serial_key:
                if p2[i] not in ' ~`!@#$%^&*()_+=-}{][|"\'<,>.?/:;\\':
                    if i % 2:
                        if p2[i] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                            collected_string.append(p2[i])
                            serial_key[i+17] = p2[i]
                            skor += 1

                    elif p2[i] not in '1234567890':
                        if p2[i] not in 'bruh':
                            collected_string.append(p2[i])
                            serial_key[i+17] = p2[i]
                            skor += 1

    if kode[32] == '-': # 32
        serial_key[32] = "-"
        skor += 1
    for i in range(15):
        if 32 <= ord(p3[i]) <= 126:
            if p3[i] not in collected_string and p3[i] not in serial_key:
                if p3[i] not in ' ~`!@#$%^&*()_+=-}{][|"\'<,>.?/:;\\':
                    if p3[i] in '69420':
                        serial_key[i+33] = p3[i]
                        skor += 1
                        continue
                    if p3[i] in 'OMEGALUL':
                        serial_key[i+33] = p3[i]
                        skor += 1
                        continue
                    if p3[i] in 'pogchamp':
                        serial_key[i+33] = p3[i]
                        skor += 1

    if kode[48] == '-': # 48
        serial_key[48] = "-"
        skor += 1

    for i in range(16):
        if 32 <= ord(p4[i]) <= 126:
            if p4[i] not in collected_string and p4[i] not in serial_key:
                serial_key[i+49] = p4[i]
                skor += 1
    # print(skor, serial_key)

import random
import string
a = string.printable[:-5]
while 1:
    if 0 not in serial_key:
        print("Token Pekalongan --> ","".join(serial_key))
        exit()
    strs = "".join([random.choice(a) for i in range(65)])
    validate(strs)
    
# token #####validate("01DCQ5U78PZHJKER-aot2y9mpAlf4IeB-GGGGGGGGGGGGGGG-OOOOOOOOOOOOOOOO") --> manual token