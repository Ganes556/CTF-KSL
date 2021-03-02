FLAG = "- R E D A C T E D -"
reverse_FLAG = FLAG[::-1]
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
    # 1422
    
    return v
  
if __name__ == "__main__": 
    n = len(reverse_FLAG)
    key = blueming(len(reverse_FLAG))
    enc = ''
    
    for i in range(n):
        enc += chr((key[i].x ^ ord(reverse_FLAG[i])) + key[i].y)
    print(enc)
    test = "?3d1S/R-K+T*g)V(S62"

    y = [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [3, 5, 7, 9, 11, 13, 15, 17, 19, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19], [5, 7, 9, 11, 13, 15, 17, 19], [6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19], [7, 11, 13, 17, 19], [8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19], [9, 11, 13, 15, 17, 19], [10, 11, 13, 14, 
16, 17, 19, 11, 13, 17, 19], [12, 13, 14, 15, 16, 17, 18, 19], [13, 17, 19], [14, 15, 16, 17, 18, 19], [15, 17, 19, 16, 17, 19], [17, 19], [18, 19], [19]]
    
#     c1 =   [63, 51, 100, 49, 83, 47, 82, 45, 75, 43, 84, 42, 103, 41, 86, 40, 83, 54, 50]

#     test2 = [45, 32, 82, 32, 69, 32, 68, 32, 65, 32, 67, 32, 84, 32, 69, 32, 68, 32, 45]
    

    

#     zip_ob = zip(c1,test2)
#     sub = []
#     for c1_i, test2_i in zip_ob:
#         sub.append(c1_i+test2_i)
    
#     for i in range(len(y)):
#         test4 = []

#     print(test4)

        
    