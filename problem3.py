lista=[]
listaprimos=[]
tope=int (600851475143)
for i in range(tope):
    if tope%(i+1)==0:
        lista.append(i+1)

for k in range(len(lista)):
    j=2
    bandera=False
    if lista[k]>1:
        while j<=lista[k]**0.5:
            if lista[k]%j==0:
                bandera=True
                j=lista[k]+1
            j+=1
        if bandera==False:
            listaprimos.append(lista[k])
print(listaprimos[-1])
