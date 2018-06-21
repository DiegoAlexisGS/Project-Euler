"""
Project Euler problem 46 code in python.
"""
import time as tm
import math,sys
from problem41 import primo
start=tm.clock()
pot=[]
odd=[]
for i in range(1,40409):
    pot.append(int(math.pow(i,2)))
for j in range(2,100000):
    if j%2==0 or primo(j)==True:
        pass
    else:
        odd.append(j)
#Proceso
for k in odd:
    for l in pot:
        bandera=False
        if int(k-2*l)>0:
            if primo(int(k-2*l))==True:
                bandera=True
                break
    if bandera==False:
        print(k,tm.clock()-start)
        sys.exit()
