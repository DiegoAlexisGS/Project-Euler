def collatz(m):
    v=m
    largo=[]
    largo.append(m)
    while m!=1:
        if m%2==0:
            m=m/2
            largo.append(m)
        else:
            m=3*m+1
            largo.append(m)
    return(len(largo),v)

tamaños=[]
n=1000000
while n>0:
    valor=collatz(n)
    tamaños.append(valor)
    n-=1

tamaños.sort()
print(tamaños[-1])
