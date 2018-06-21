"Project Euler. Problem 38 code in python"
import time
start=time.clock()
compara=123456789
valor=0
for i in range(2,9999):
    num=""
    n=1
    bandera=True
    lis=[]
    val2=""
    while bandera==True:
        val=str(i*n)
        num+=val
        if len(num)==9:
            for k in num:
                lis.append(k)
            lis.sort()
            for l in lis:
                val2+=l
            if int(val2)==compara:
                if valor<int(num):
                    valor=int(num)
            bandera=False

        elif len(num)>9:
            bandera=False
        n+=1
print(valor,time.clock()-start)
