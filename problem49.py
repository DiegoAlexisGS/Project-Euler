"""
Project Euler problem 49 code in python by Alexis Galois
"""
import time, itertools,sys
from problem41 import primo
start=time.clock()
lista=[]
for i in range(1000,10000):
    if primo(i)==True:
        lista.append(i)
for j in lista:
    lista2=[]
    for k in lista:
        if set(str(j))==set(str(k)) and j!=k:
            lista2.append(k)
    for l in lista2:
        for m in lista2:
            if m<l:
                dif=l-m
                if l+dif in lista2 and m!=1487:
                    print(str(m)+str(l)+str(l+dif))
                    print(time.clock()-start)
                    sys.exit()
