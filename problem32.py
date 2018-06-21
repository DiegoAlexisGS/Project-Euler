import time
start=time.clock()
n=[1,2,3,4,5,6,7,8,9]

def comprueba(a,b):
    lista0=[]
    a1=str(a)
    b1=str(b)
    c1=str(a*b)
    d1=a1+b1+c1
    total=len(d1)
    for p in d1:
        lista0.append(int(p))
    return(total,d1,c1,lista0)

listatotal=[]
for i in range(2000):
    for j in range(2000):
        valor=sorted(comprueba(i+1,j+1)[3])
        if valor==n:
            listatotal.append(comprueba(i+1,j+1)[2])
#suma
lista3=[]
suma=0
lista3=list(set(listatotal))
for m in lista3:
    suma+=int(m)
print(suma,time.clock()-start)
