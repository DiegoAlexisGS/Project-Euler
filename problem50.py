"""
Project Euler problem 50 code in python
"""
import time
from problem41 import primo
start=time.clock()
lista=[]
val2=0
num2=0
k=0
bandera=False
for i in range(1,1000001):
    if primo(i)==True:
        lista.append(i)
def valores(lista,inic):
    val=0
    num=0
    n=0
    lis=lista[inic:]
    while num<1000000:
        num+=lis[n]
        if primo(num)==True and val<num:
            val=num
        n+=1
    return(val)

while num2<1000000:
    num2=valores(lista,k)
    if num2>val2 and num2<1000000:
        val2=num2
    k+=1
print(val2,time.clock()-start)
