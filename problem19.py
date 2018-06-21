"""
Definimos lo necesario
asignamos a cada mes y a cada día un valor. Para meses el núm. de días
y para días del 1 al 7 de lunes a domingo.
"""
dias=1
january=31
febrary=28
march=31
april=30
may=31
june=30
july=31
august=31
september=30
october=31
november=30
december=31
lunes=1
martes=2
miercoles=3
jueves=4
viernes=5
sabado=6
domingo=7
meses=[january,febrary,march,april,may,june,july,august,september,october,november,december]
dias=[lunes,martes,miercoles,jueves,viernes,sabado,domingo]
##print(meses)
"""
Definimos una función que calcula el número de de domingos que son primer día de mes
y regresa el primer dia en el que incia el mes siguiente
"""
def dmeses(mes,dia,año):
    cuenta=0
    if año%4==0:  ##si el año es bisciesto agrega un día a febrero
        meses[1]=29
    else:
        meses[1]=28
    day=1   ##La variable dia funciona como contador
    dif=7-dia    ##Calcula la diferencia entre el día inicial y el domingo que tiene valor 7
    day=day+dif   ##se la asigna a day el valor de los domingos##
    if day==1:    ##Si un domingo tiene valor 1 es inicio de mes y se agrega a cuenta un uno
        cuenta+=1
    for i in range(4): ##Itera por cuatro semanas
        day+=7         ##Aumenta a day 7 dias para calcular los domingos
        if day==1:
            cuenta+=1
        if day>mes:    ##Si el mes no tiene necesariamente un domingo en la cuarta semana no se agrega nada
            day-=7
    valores=[mes-day+1,cuenta] ##Vector con la suma de los domingos de inicio de mes y el dia de inicio del mes siguiente
    return(valores) ##Regresa el valor


cuenta=0 ##Cuenta suma los valores de cada año en los que hay domingos como inicio de meses
perro=[2,0]  ##Vector inicial del años 1901
for a in range(100): ##Itera por cien años
    for j in range(12):  ##Itera por doce meses(un año a la vez)
        perro=dmeses(meses[j],perro[0],1901+a)   ##Inicializa la función con los valores inciales y después con los que salgan de la función
        cuenta+=perro[1] ##Suma el valor de domingos encontrados como inicio de mes en el año examinado
print("El valor es ", cuenta," ",1901+a) ##Muestra el valor de los domingos y el año final.
