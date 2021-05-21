import base64

def encrypt(plain,key):
    result = ""
    
    for i in range(len(plain)):
        result += chr(ord(plain[i]) ^ ord(key[i%len(key)]))
    return result

flag1 = base64.decodebytes(open("flag.enc","rb").read()).decode()
key1 = open("desc2.txt","r").read() 

flag2 = encrypt(flag1,key1)
key2 = base64.decodebytes(open("desc.enc","rb").read()).decode()

pureFlag = encrypt(flag2,key2)
print(pureFlag)


# find part of key
# part_flag = "KSL2020{"
# for i in range(len(flag)):
#     candidate = encrypt(flag[i:i+len(part_flag)], part_flag)
#     if candidate.isalnum():
#         print(candidate)