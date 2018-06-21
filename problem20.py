
def factorial(n):
    fac=1
    for i in range(n):
        fac=fac*((n-1)-(i-1))
    return(fac)


print(factorial(100))
suma=0
num=str(factorial(100))
for i in range(len(num)):

    suma=suma+int(num[i])
print(suma)
