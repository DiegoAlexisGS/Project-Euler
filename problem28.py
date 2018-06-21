import numpy as np
numeros=np.array(np.arange(1002001)+1)
incrementos=list()
#crea la lista de incrementos necesarios
for p in range(500):
    incrementos.append(2*(p+1))


#Localizador de diagonales
def localizador(vector):
    suma=0
    n=0
    for i in incrementos:
        for j in range(5):
            if i==2 and j==0:
                suma+=vector[j*i+n]
            elif j==0:
                pass
            else:
                suma+=vector[j*i+n]
        n=j*i+n
    return(suma)


print(localizador(numeros))
