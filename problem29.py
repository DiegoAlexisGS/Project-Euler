lista=list()
potencias=list()
for p in range(99):
    lista.append(2+p)
print(lista)

#Genera potencias
for i in lista:
    for j in lista:
        potencias.append(i**j)


print(len(list(set(potencias))))
