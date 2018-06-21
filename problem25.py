from time import time

tiempo_inicial=time()
def fibonacci(n):
    seria=[]
    seria.append(0)
    seria.append(1)
    for i in range(n):
        seria.append(seria[i]+seria[i+1])
        valor=seria[i]+seria[i+1]
        tam=len(str(seria[i]))
        if tam==1000:
            print(tam)
            return(i)
            break


print(fibonacci(1000000))

tiempo_final=time()
print(tiempo_final-tiempo_inicial)
