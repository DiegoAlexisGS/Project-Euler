
n=600851475143
n2=60085147514
seccion=60085147514
tope=int (n/2)
primo=0
cont=1
j=1
bandera=False
for i in range(seccion):
    j=1
    bandera=False
    if n%(i+1)==0:
        while j<=(i+1)**0.5:
            if j>1:
                if (i+1)%j==0:
                    bandera=True
                    j=i+1
            j+=1
        if bandera==False:
            primo=i+1

print(primo)
print(i+1)
