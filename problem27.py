#Numbers prime
def primo(n):
    bandera=False
    n=abs(n)
    for i in range(int(n**(1/2))):
        if n%(i+1)==0 and i+1!=1:
            bandera=True
            return(0)
            break
    if bandera==False:
        #print("Primo",n)
        return(1)

#Program about problem 27
def cuentas(a,b):
    m=0
    cuenta=0
    while primo(m**2+a*m+b):
        cuenta+=int(primo(m**2+a*m+b))
        m+=1
    return(cuenta,a,b)

#Iteración de a y b
a=-999
cuenta2=0
b=-1000
for i in range(1998):
    b=-1000
    for j in range(2000):
        b+=1
        re=cuentas(a,b)
        if cuenta2<re[0]:
            cuenta2=re[0]
            print(cuenta2,a,b,a*b)
    a+=1
