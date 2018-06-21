"""
Project Euler problem 44. Code in python.
Alexis Galois
"""
import time
import itertools
start=time.clock()
lista=[]
def resta(a,b):
    return(abs(a-b))
def suma(a,b):
    return(abs(a+b))
for i in range(1,10001):
    lista.append(int(i*(i*3-1)/2))
comb=list(itertools.combinations(lista[:5001],2))
results=list(set(itertools.starmap(resta,comb)))
results1=list(set(itertools.starmap(suma,comb)))
for j in range(len(results)):
    if results[j] in lista[:5001]:
        if results1[j] in lista:
            print(results[j])
            break
print(time.clock()-start)
#594.97
