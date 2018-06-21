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

primos=[]
j=0
p=0
while len(primos)<10001:
    if primo(j)==True:
        primos.append(j)
    j+=1


print(primos)
print(len(primos))
print(primos[10000])
