"""
Project Euler problem 49 code in python by Alexis Galois
"""
import time, itertools
from problem41 import primo
start=time.clock()
lista=[]
val="0123456789"
per=list(itertools.permutations(val,4))
for i in per:
    val2=""
    for j in i:
        val2+=j
    if primo(int(val2))==True and len(str(int(val2)))==4:
        lista.append(int(val2))
#Permutaciones
for k in lista:
    valores=[]
    for l in lista:
        if len(set(str(k)+str(l)))==4 and k!=l:
            valores.append(l)
    valores=sorted(valores)
    for m in valores:
        for n in valores:
            if m<n:
                dif=n-m
                if n+dif in valores:
                    print(m,n,n+dif)
print(time.clock()-start)
