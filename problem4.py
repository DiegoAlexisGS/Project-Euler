i=0
j=0
lista_num=[]
n=999
m=999
while j<999:    #Multiplica de 999 a 100 por los números del 999 al 100
    i=0
    n=999-j       #Resta 999-j para obtener en cada iteración 999,998,997.....etc
    while i<999:    #Multiplica cada número por los números 999 al 100
        nums=str(n*(999-i))
        if 999-i>99:           #Solo lo hace si 999-i es mayor a 99
            if nums[0]==nums[-1]:
                if nums[1]==nums[-2]:
                    if len(nums)==6:
                        if nums[2]==nums[-3]:
                            nums=int(nums)
                            lista_num.append(nums) #Agrega a la lista lo números palindronos de seis cifras
        i+=1
    j+=1

lista_num.sort()     #Ordena la lista de menos a mayor
print(lista_num)     #imprime la lista entera
print(lista_num[-1]) #Imprime el mayor número
