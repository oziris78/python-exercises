
print()
print()


def add(dz):
    tp = 0
    for i in range(0,len(dz)):
        tp += dz[i]
    
    return tp

def mul(dz):
    çr = 1
    for i in range(0,len(dz)):
        çr *= dz[i]
    
    return çr

def my_max(dz):
    return max(dz)

def my_min(dz):
    return min(dz)

def two_or_same(dz):
    sayac = 0
    for i in range(0,len(dz)):
        s = str(dz[i])
        if (s[len(s)-1] is s[0]) and len(s)>=2:
            sayac += 1
    
    return sayac
            
def is_unique(dz):
    return list(set(dz))

def is_empty(dz):
    if len(dz)==0:
        return True

    return False

def longs(dz, n):
    dz2 = list()
    for i in range(0, len(dz)):
        s = str(dz[i])
        if len(s)>n:
            dz2.append(s)
    
    return dz2

def has_common(dz1,dz2):
    for i in dz1:
        for j in dz2:
            if i == j:
                return True

    return False

def print_odds(dz):
    dz2 = list()
    for i in range(0, len(dz)):
        if dz[i]%2==1:
            dz2.append(str(dz[i]))
        
    print(dz2)

def list_diff(dz1,dz2):
    dz3 = set(dz1)
    dz4 = set(dz2)
    dz5 = dz3.difference(dz4)
    return list(dz5)

def list_to_str(dz):
    s = str()
    for i in range(0,len(dz)):
        s += str(dz[i])
        
    return s

def append_list_to_end(dz1,dz2):
    dz3 = dz1
    for i in range(0,len(dz2)):
        dz3.append(dz2[i])
    
    return dz3

def frequency(dz,s):
    sayac = 0
    for i in range(0,len(dz)):
        if str(s) == str(dz[i]):
            sayac += 1
            
    return sayac

def Dizelgeiçerme(dz):
    for i in range(0,len(dz)):
        if type(dz[i]) is list:
            return True
        
    return False

def sabitdizelgemi(dz):
    sayac = 0
    for i in range(0,len(dz)-1):
        if str(dz[i]) == str(dz[i+1]):
            sayac = sayac + 1 
    
    if sayac == len(dz)-1:
        return True
    else:
        return False

def enbdizelge(dz):
    indeks = 0
    toplam = 0
    enb = -99999999999999999
    for i in range(0,len(dz)):
        for j in range(0,len(dz[i])):
            toplam += dz[i][j]
            
        if toplam>enb:
            enb = toplam
            toplam = 0
            indeks = i
            
    return dz[indeks]
         

def büyükolanlar(dz,c):
    dz2 = list()
    for i in range(0,len(dz)):
        if int(dz[i])>c:
            dz2.append(dz[i])
    
    return dz2
    
def düzle(dz):
    dz2 = list()
    for i in range(0,len(dz)):
        if (type(dz[i]) is str) or (type(dz[i]) is int):
            dz2.append(dz[i])
        elif type(dz[i]) is list:
            for j in range(0,len(dz[i])):
                dz2.append(  dz[i][j]  )
        
    return dz2        
   
   







print()
print()

