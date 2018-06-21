import numpy as np

fibo=np.zeros(4000000)
fibo[0]=1  #Primer número de la serie de Fibonacci
fibo[1]=1  #Segundo número de la serie de Fibonacci
suma=0     #suma de los números pares
print(fibo)
#For que crea la serie hasta 4000000
for i in range(len(fibo)):
    if i>1:
        fibo[i]=fibo[i-1]+fibo[i-2]  #Le suma al elemento i apartir de i=2 los dos anteriores
        if fibo[i]<4000000: #Si el valor es menor a 4000000
            if fibo[i]%2==0: #Si el valor es par
                suma+=fibo[i] #Suma el valor al final

#imprime la suma y el vector de fibonacci
print(fibo)
print(suma)
