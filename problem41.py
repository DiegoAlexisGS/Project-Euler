import time
start=time.clock()
def primo(n):
    bandera=True
    if n==0 or n==1:
        bandera=False
    else:
        for i in range(int(n**0.5)):
            if n%(i+1)==0 and (i+1)!=1:
                bandera=False
                break
    return(bandera)

def pandigital(m):
    lista=[]
    comprueba=""
    num=""
    for i in str(m):
        lista.append(i)
    for j in range(len(lista)):
        comprueba+=str(j+1)
    lista.sort()
    for k in lista:
        num+=k
    if int(comprueba)==int(num):
        return(True)
    else:
        return(False)
"""
a=0
for i in range(7600000,8000000):
    if primo(i)==True and pandigital(i)==True:
        if a<i:
            a=i
            print(a)

print(time.clock()-start,a)
"""
