#función que devuelve el factor primo menor de n
def primo(n):
    i=1
    bandera=False
    tope=int(n**0.5)
    for i in range(tope):
        bandera=False
        if n%(i+1)==0 and i+1>1:
            bandera=True
            break
    if bandera==False:
        i=n-1
    return(i+1)

#Regresa el mayor factor primo
n=600851475143  #Número a evaluar
prim1=0         #Variable auxiliar
bandera2=False  #Indicador
while bandera2==False:    #Bucle que me obtiene y compara los factores primos
    prim=int(primo(n))
    n=int(n/prim)
    if prim1<prim:        #Compara que factor es mayor el anterior o el nuevo en cada iteración
        prim1=prim
    if n==1:              #Si el cociente da 1 quiere decir que el último factor ya es primo
        bandera2=True
print(prim1)              #El último factor es impreso en pantalla
