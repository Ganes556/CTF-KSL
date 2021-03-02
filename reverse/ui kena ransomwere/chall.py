
# flag = "- R E D A C T E D -"
flag = "Dudale``oWjYQKOKJAZYDR]NWYJ kucÜiÜ$ÐÒÜ:uÜ	ÞyÞ cql`YhRbgQlUFJ]GNq]£¢µ«¯­¶¹{¹gie¹l¬u®½ªµª¨¹_@]gu5_\$lW#d__a�è"
# flag = "-RE813D9$"

# flag = open("flag.enc","r")

# open("dec.text", "w").write(__import__('base64').b64decode(''.join([chr(x) 
# for x in (lambda x: (lambda p: [(i ^ ord(j) - p[i] & 0xff) 
# for i, j in enumerate(flag.read())])(x))([x for x in range(len(flag.read()))])])))

# a = ''.join([chr(x) for x in (lambda x: (lambda p: [(i ^ ord(j) - p[i] & 0xff)
# for i, j in enumerate(flag)]) (x)) ([x for x in range(len(flag))])])

# yang lebih besar angkanya itu yang duluan di operasikan didalam xor
b = ''.join([chr(x) for x in (lambda x: (lambda p: [((i^ord(j)) + p[i] & 0xff)
for i, j in enumerate(flag)]) (x)) ([x for x in range(len(flag))])])
print(b)


