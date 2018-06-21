"Project Euler. Problem 35 code in python by Alexis Galois"
import time as tm
start=tm.clock()
#Return the number n if it is prime
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

#It rotate the digits
def permuta(mlista):
    a=mlista[0]
    lista2=[]
    for i in range(len(mlista)-1):
        lista2.append(mlista[i+1])
    lista2.append(a)
    return(lista2)

#Process
cuenta=0
for i in range(1000000):
    lista3=[]
    if primo(i)==True:
        bandera=True
        for j in str(i):
            lista3.append(j)
        vallis=lista3[:]
        for k in range(len(lista3)-1):
            num=""
            vallis=permuta(vallis)
            #Recombierte el número
            for i in vallis:
                num+=i
            if primo(int(num))==False:
                bandera=False
                break
        if bandera==True:
            cuenta+=1
print(cuenta)
print(tm.clock()-start)
