import numpy as np
"""
Problema 18 project Euler.
"""
##Esto me abre el archivo y me lo pasa todo a
##Una lista de listas
piramide=open("piramide.txt","r")
lineas=[]
for i in range(100):
    linea=piramide.readline()
    linea=linea.split(" ")
    lineas.append(linea)
piramide.close()

def triangulo(p,s,t):
    if p+s<s+t:
        return(s+t)
    else:
        return(p+s)
#Programa general
tope=len(lineas)
for i in range(tope):
    tope2=(tope-i-1)
    for j in range(tope2):
        v1=int(lineas[tope-1-i][j])
        v2=int(lineas[tope-2-i][j])
        v3=int(lineas[tope-1-i][j+1])
        lineas[tope-2-i][j]=triangulo(v1,v2,v3)
print(lineas[0][0])
