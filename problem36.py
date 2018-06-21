"Project Euler. Problem 36 code in python"
import time
start=time.clock()
def palindromic(n):
    lista=[]
    lista2=[]
    num=""
    for i in str(n):
        lista.append(i)
    for i in range(len(lista)):
        lista2.append(lista[-(i+1)])
    for i in lista2:
        num+=str(i)
    return(num)

def binario(n):
    binario=[]
    a=n
    num=""
    while a!=1:
        binario.append(a%2)
        a=int(a/2)
    binario.append(1)
    for i in range(len(binario)):
        num+=str(binario[len(binario)-1-i])
    return(num)

cuenta=0
for z in range(1,1000000):
    if z==int(palindromic(z)):
        a=binario(z)
        a2=palindromic(a)
        if a==a2:
            cuenta+=z

print(cuenta)
print(time.clock()-start)
