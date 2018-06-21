import time
start=time.clock()
val=""
n=1
total=1
while len(val)<1000001:
    val+=str(n)
    n+=1
for i in range(7):
    total*=int(val[10**i-1])
print(total,time.clock()-start)
