"""
CALCULA TODOS LOS VALORES ABUNDANTES
"""
from time import time



def abundant(n):
    abundantlist=[]
    sumatotal=0
    for i in range(int((n+1))):
        suma=0
        for j in range(int(i/2)):
            if i%(j+1)==0:
                suma+=j+1
        if suma>i:
            sumatotal+=1
            abundantlist.append(i)
    return(abundantlist)

"""
LISTA TODOS LAS SUMAS DE DOS NÚMEROS ABUNDANTES MENORES A UN TOPE
"""
def sumadetodos(listas,tope):
    sumandos=[]
    copia=listas[:]
    for i in range(len(listas)):
        for j in range(len(copia)):
            valor=copia[j]+listas[i]
            if valor<=tope:
                sumandos.append(valor)
    sumandos.sort()
    return(sumandos)

"""
SUMA TODAS LAS POSIBLES SUMAS DE NÚMEROS AUNDANTES MEORES A UN TOPE
"""
def resume(lista2):
    suma=0
    lista_resumida=list(dict.fromkeys(lista2).keys())
    for i in range(len(lista_resumida)):
        suma+=lista_resumida[i]
    return(suma)

tiempo_inicial=time()
tope=28123 ##TOPE DE LOS VALORES
valores=resume(sumadetodos(abundant(28123),28123)) #lA SUMA DE TODAS LAS SUMAS
print(tope*(tope+1)/2-valores) #DIFERENCIA DE LA SUMA DE TODOS LOS NÚMEROS Y LA SUMA DE LOS NÚMEROS ABUNDANTES NOS DA LA SUMA DE LOS
#NUÚMEROS QUE NO SE PUEDEN EXPRESAR COMO SUMA DE DOS NÚMEROS ABUNDANTES
tiempo_final=time()
tiempo_ejecucion=tiempo_final-tiempo_inicial
print(tiempo_ejecucion)
