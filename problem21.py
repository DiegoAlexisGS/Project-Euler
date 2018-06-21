"""
función que cambia calcula la suma de divisores propios
"""
def amicable(n):
    tope=int(n/2)
    suma=0
    divisores=[]
    for i in range(tope):
        if n%(i+1)==0:
            divisores.append(i+1)
    for j in range(len(divisores)):
        suma+=divisores[j]
    return(suma)

"""
Aquí empieza el programa. Usamos la función sobre el número y sobre la suma de los divisores del número
si son iguales son números amigos y los sumamos en un total
"""
s=10000
sumad=0
for a in range(s):
    if a>1:
        valor=amicable(a)
        valor2=amicable(valor)
        if a==valor2 and a!=valor:
            ##print("Son amigos ",a,"and ",valor )
            sumad+=a+valor
print(int(sumad/2))
