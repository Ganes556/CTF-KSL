gambarnya = open("gambar1.png","rb").read()
pic =  gambarnya.replace("GKSK","").replace(chr(255),"").replace(chr(170),"").replace("SADF","").replace("QWER","")
open("solve.png","wb").write(pic)