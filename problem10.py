
def primo(n):
    bandera=True
    tope=int(n**0.5)
    i=0
    if n==0:
        bandera=False
        return(False)
    while i<tope:
        if n==1:
            bandera=False
            return (False)
        if i+1>1 and n>1:
            if n%(i+1)==0:
                bandera=False
                return (False)
                break
        i+=1
    if bandera==True:
        return(True)

i=2
suma=0
while i<2000000:
    primo(i)
    if primo(i)==True:
        suma=suma+i
    i+=1
print(suma)
