
#n=600851475143 #71,839,1471
n=6857

i=1
bandera=False
tope=int(n**0.5)
for i in range(tope):
    bandera=False
    if n%(i+1)==0 and i+1>1:
        print("El numero no es primo",i+1)
        bandera=True
        break
if bandera==False:
    print("primo",i+1)
