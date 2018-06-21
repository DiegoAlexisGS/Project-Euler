def generet(n):
    suma=0
    for i in range(n+1):
        suma=suma+i
    return(suma)
#Comprobamos cual de estos numeros tiene 500 divisores
m=10000
bandera=False
for i in range(m):
    d=1
    contar=0
    valor=generet(i)
    tope=int (valor/2)
    while d<=tope:
        if valor%d==0:
            contar+=1
        d+=1
    if contar==100 or contar>100:
        print("tengo ",contar," divisores")
    if contar==400 or contar>400:
        print("Tengo ",contar," divisores")
    if contar==500 or contar>500:
        print("No hubo")
        bandera=True
        break

if bandera==True:
    print(valor)
else:
    print("No hay con ",m)
