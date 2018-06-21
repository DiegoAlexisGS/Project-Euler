from time import time
tiempo_inicial=time()
div=[]
g=0
num=0
#Llena la lisa del 1 al 999
for i in range(999):
    div.append(i+1)
#Busca la longitud de la cadena
def buscador(n):
    contador=0
    residuo=[]
    perro=False
    m=1
    while m<n:
        m=m*10
    m=m%n
    residuo.append(m)
    while perro==False:
        contador+=1
        while m<n and m!=0:
            m=m*10

        m=m%n
        if m==residuo[0]:
            perro=True
        else:
            if m==0 or contador==2000:
                perro=True
            residuo.append(m)
    return(n,len(residuo))


#Prueba con todos los numeros de la lista
for i in div:
    mayor=[]
    mayor=buscador(i)
    if mayor[1]<2001:
        print(mayor)
        if mayor[1]>g:
            num=mayor[0]
            g=mayor[1]

print(num)
