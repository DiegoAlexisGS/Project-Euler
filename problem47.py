"""
Project Euler problem 47 code in python
Alexis Galois
"""
import time,sys
from problem41 import primo
start=time.clock()
primos=[]
n=1
bandera=False
for i in range(1,1001):
    if primo(i)==True:
        primos.append(i)
def contar(n):
    contador=0
    divi=[]
    for j in primos:
        if n%j**2==0:
            n=int(n/j**2)
            divi.append(j)
        if n%j==0:
            n=int(n/j)
            divi.append(j)
            divi=list(set(divi))
            if n==1 and len(divi)==4:
                return(True)
                break
    return(False)
while bandera==False:
    if contar(n)==True and contar(n+1)==True and contar(n+2)==True and contar(n+3)==True:
        bandera=True
    n+=1
print(n-1,n,n+1,n+2,time.clock()-start)
