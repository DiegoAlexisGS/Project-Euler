def numero(n):
    return list(map(int,str(n)))


#Verifica si es o no es un número querido
lista=[]
total=0
for i in range(1000000):
    tam=numero(i)
    suma=0
    for j in tam:
        suma+=j**5
    if i==suma:
        lista.append(i)
        total+=i

print(lista,len(lista),total-1)
