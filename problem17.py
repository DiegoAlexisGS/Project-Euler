import time as tm
import inflect
fl=inflect.engine() #sirve para obtener un numero en letras(ingles)

#Función que regresa el numero de letras
def tranform(n):
    numero=""
    numero2=""
    num=fl.number_to_words(n)
    #Primera transformación
    num=num.split(" ")
    #Rehace la lista
    tam=len(num)
    for i in range(tam):
        numero=numero+num[i]
    #Segunda transformación
    numero=numero.split("-")
    #Rehace el número
    tam=len(numero)
    for j in range(tam):
        numero2=numero2+numero[j]
    return(len(numero2))

p=1000
suma=0
for m in range(p):
    suma+=(tranform(m+1))
print(suma)
