"""
Project Euler problem 45 code in python.
Alexis Galois
"""
import itertools,time
start=time.clock()
lista=[]
lista2=[]
lista3=[]
result=[]
for i in range(1000000):
    lista.append(int(i*(i+1)/2))#T
    lista2.append(int(i*(3*i-1)/2))#p
    lista3.append(int(i*(2*i-1)))#h
sets=[set(lista),set(lista2),set(lista3)]
result=list(set.intersection(*sets))
print(result,time.clock()-start)
