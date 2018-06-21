"""
Project Euler. Problem 42. Code in python
Alexis Galois
"""
import time
import string
start=time.clock()
archivo=open("words.txt","r")
linea=archivo.read()
linea=linea.split(",")
archivo.close()
abc=string.ascii_uppercase

total=0
def genera():
    lista=[]
    for i in range(25):
        n=0.5*((i+1)+1)*(i+1)
        lista.append(int(n))
    return(lista)

trian=genera()
for k in linea:
    suma=0
    for i in k:
        for j in range(len(abc)):
            if i==abc[j]:
                suma+=(j+1)
    for l in trian:
        if suma==l:
            total+=1
print(total,time.clock()-start)
