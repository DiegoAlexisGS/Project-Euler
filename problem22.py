"""
Aquí se habré el programa
"""
archivo=open("p022_names.txt","r")
linea=archivo.readlines()
nombres=linea[0]
archivo.close()
nombres=nombres.split(',')
nombres.sort()

def abc(nombre):
    suma=0
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(nombre)):
        letra=nombre[i]
        for j in range(len(alpha)):
            if letra==alpha[j]:
                suma+=j+1
    return(suma)
"""
Aquí empieza el programa que necesitamos para el problema
"""
total=0
for nom in range(len(nombres)):
    producto=0
    no=str(nombres[nom])
    part1=abc(no)
    producto=part1*(nom+1)
    total+=producto
print(total)
