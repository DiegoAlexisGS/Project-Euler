"Project Euler. Problem 37 code in python"
import time
start=time.clock()
def primo(n):
    bandera=True
    if n==0 or n==1:
        bandera=False
    else:
        for i in range(int(n**0.5)):
            if n%(i+1)==0 and (i+1)!=1:
                bandera=False
                break
    return(bandera)

def truncar(lista):
    t=len(lista)
    lista.pop(t-1)
    return(lista)

def truncal(lista):
    t=len(lista)
    lista.pop(0)
    return(lista)

cuenta=0
cont=10
suma=0
while cuenta<11:
    if primo(cont)==True:
        bandera=True
        ltr=[]
        for i in str(cont):
            ltr.append(i)
        val=ltr[:]
        val2=ltr[:]
        for j in range(len(ltr)-1):
            num=""
            num2=""
            val=truncal(val)
            val2=truncar(val2)
            for k in range(len(val)):
                num+=val[k]
                num2+=val2[k]
            if primo(int(num))==False or primo(int(num2))==False:
                bandera=False
                break
        if bandera==True:
            suma+=cont
            cuenta+=1
    cont+=1
print(cuenta,suma,time.clock()-start)
