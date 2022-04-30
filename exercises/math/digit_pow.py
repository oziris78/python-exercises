

from math import pow

def basamakUssuEsit(limit, h, n):
    basamakToplam = int(0)
    dzl = list()
    for i in range(limit, limit+h+1):
        i = str(i)
    
        for j in i:
            j = int(j)
            basamakToplam += pow(j, n)
            
        if(int(i) == basamakToplam):
            dzl.append(i)
            
        basamakToplam = 0
    
    return dzl


with open("usEsitMi.txt", "a+") as dsy:
    for i in range(1,11):
        dsy.write(f"{i}: " + str(basamakUssuEsit(1000000,1000000,i)) + "\n")
   
    