"""
Problema 18 project Euler.
"""
##Esto me abre el archivo y me lo pasa todo a
##Una lista de listas
piramide=open("piramide.txt","r")
lineas=[]
for i in range(4):
    linea=piramide.readline()
    linea=linea.split(" ")
    lineas.append(linea)
piramide.close()

def mayor(p,s):
    if p<s:
        return(s)
    else:
        return(p)

##Aquí empezaremos
def reducc(listas):
    newlist=[]

    tope=len(listas)
    for i in range(tope):
        nl=[]
        tope2=len(listas[tope-1-i])
        for j in range(tope2):
            if j==0 and tope-i>1:
                valor=int(listas[tope-1-i][j])
                valor2=int(listas[tope-1-i][j+1])
                valor3=int(listas[tope-2-i][j])
                #Suma
                valor=valor+valor3
                valor2=valor2+valor3
                nl.append(mayor(valor,valor2))
            elif j<tope2-1:
                valor=int(listas[tope-1-i][j])
                valor2=int(listas[tope-1-i][j+1])
                valor3=int(listas[tope-2-i][j])
                valor=valor+valor3
                valor2=valor2+valor3
                nl.append(mayor(valor,valor2))
        newlist.append(nl)
    print(newlist)
        #Valores diferentes del primero y el segundo

reducc(lineas)
