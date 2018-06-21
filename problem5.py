"""
Problem number 5 of ProjectEuler
The algoritmo divides all number between 1 to 20
when finds one number that is divisible by 1 to 20
the bucle is closed and shows that number
""" 
n=360360
bandera=False
j=0
cuenta=0
while bandera==False:
    cuenta=0
    for i in range(20):
        if n%(i+1)==0:
            cuenta+=1
            if cuenta==20:
                bandera=True
                break
        else:
            break
    n+=1
print(n-1)
