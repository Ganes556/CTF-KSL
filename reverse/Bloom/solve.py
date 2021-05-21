from random import randint
def serial():
    integr = "0123456789"
    pjg = len(integr)-1
    hsil = ""
    for i in range(14):
        hsil += integr[randint(0,pjg)]
    return hsil
def check():
    s = 0
    v6 = 0
    v7 = 0 
    v8 = 0 
    v9 = 0 
    v10= 0 
    v11= 0 
    v12= 0 
    v13= 0 
    v14= 0 
    v14= 0 
    v16= 0 

    i = ['a']*14
    i[0] = 75
    i[4] = 45
    i[9] = 45
    i[7] = 83
    i[8] = 82
    i[12] = 67
    i[13] = 67
    skor =0
    
    ranges = 125
    s = 0
    while 1:
        # s v6 v7 v8 v9 v10 v11 v12 v13 v14 v15 v16 
        r1 = randint(48,96)
        r2 = randint(48,96)
        # if (5 * (r1 + 100) - 870) < 9: # s
        #     s = r1
        if (10 * i[0] + r2 - 814) < 0x15: # v6
            i[1] = r2
        if (13 * (r1 - 75)) == 65: #v7
            i[2] = r1
        if 13 * r1 == 988: # v8
            i[3] = r1

        if r1 == 45 and r2 == 45: # v9 v14
            i[4] = r1
            i[9] = r2
        
        if (25 - r1 / 3) < 4: # v10
            i[5] = r1

        if (300 * r1 - 22440) < 0x83: #v11
            i[6] = r1

        if 21 * r1 == 1365: #v15
            i[10] = r1
        if (32 * r1 - 2457) < 0x5A: #v16
            i[11] = r1
      
        for z in i:
            if type(z) == type(0):
                skor +=1
        if skor == 10:
            ranges = 125
        if skor == 14:
            print(i)
            return "".join([chr(z) for z in i])
            # print(i)
            
      
        skor = 0
# serial key valid KTPL-@KSR-AOCC


key = check()
print(key)

