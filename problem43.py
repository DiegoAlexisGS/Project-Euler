"""
Project Euler. Problem 43. Code in python.
Alexis Galois
"""
import itertools as it
import time
start=time.clock()
numbers="0123456789"
lista=list(it.permutations(numbers,10))
lista2=[]
num=""
total=0
def comprueba(listas):
    num1=listas[1]+listas[2]+listas[3]
    num2=listas[2]+listas[3]+listas[4]
    num3=listas[3]+listas[4]+listas[5]
    num4=listas[4]+listas[5]+listas[6]
    num5=listas[5]+listas[6]+listas[7]
    num6=listas[6]+listas[7]+listas[8]
    num7=listas[7]+listas[8]+listas[9]
    primos=[2,3,5,7,11,13,17]
    nums=[num1,num2,num3,num4,num5,num6,num7]
    bandera=True
    val=""
    for i in range(len(nums)):
        if int(nums[i])%int(primos[i])!=0:
            bandera=False
            break
    if bandera==True:
        for i in listas:
            val+=str(i)
        return(int(val))
    else:
        return(0)

for i in range(len(lista)):
    total+=comprueba(lista[i])

print(total,time.clock()-start)
