"Project Euler problem 34. Code in python by Alexis Galois"

from math import factorial
total=0
for i in range(10,100000):
    suma=0
    for j in str(i):
        suma+=factorial(int(j))
    if suma==i:
        total+=i
        print(i,suma)
print(total)
