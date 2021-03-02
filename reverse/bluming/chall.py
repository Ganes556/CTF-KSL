# FLAG = "- R E D A C T E D -"
FLAG = "?3d1S/R-K+T*g)V(S62"
class Term: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
  
def gcd(a, b): 
    if b == 0: 
        return a 
    return gcd(b, a % b) 

def blueming(n): 
    v = [] 

    for i in range(1, n + 1): 
        for j in range(i + 1, n + 1): 

            if gcd(i, j) == 1: 
                v.append(Term(i, j)) 
    for i in range(len(v)): 
        for j in range(i + 1, len(v)): 
            if (v[i].x * v[j].y > v[j].x * v[i].y): 
                v[i], v[j] = v[j], v[i]         
    return v
  
if __name__ == "__main__": 
    n = len(FLAG)
    key = blueming(len(FLAG))
    enc = ''
    for i in range(n):
      enc += chr((key[i].x ^ ord(FLAG[i])) - key[i].y)
    print(enc)
    # open("flag.enc", "w+").write(enc)