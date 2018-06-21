"Project Euler. Problem 39 code in python"
import time
start=time.clock()
def comprueba(a,b,c):
    if a<b+c and b<a+c and c<a+b:
        return(True)
    else:
        return(False)
val=0
valor=0
total=0
#perimetro
for i in range(10,1001):
    val=0
    for j in range(int(i/2)):
        for k in range(int(i/2)):
            c=(j**2+k**2)**0.5
            if j+k+c==i and comprueba(j,k,c)==True and (c-abs(int(c)))==0:
                val+=1
    if total<val:
        total=val
        valor=i

print(total/2,valor,time.clock()-start)
