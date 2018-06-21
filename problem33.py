#Return the digits list of n
def digitos(n):
    dig=[]
    for i in str(n):
        dig.append(i)
    return dig
#Search the numbers without triviak cases
co=[]
co2=[]
for i in range(11,100):
    for j in range(11,100):
        if i/j<1 and i%10!=0 and j%10!=0:
            comp=i/j
            p=digitos(i)
            p1=digitos(j)
            for z in range(len(p)):
                for w in range(len(p1)):
                    if p[z]==p1[w]:
                        a=p[:]
                        a.pop(z)
                        b=p1[:]
                        b.pop(w)
                        a2=int(a[0])
                        b2=int(b[0])
                        if a2/b2==comp:
                            co.append(a2)
                            co2.append(b2)
result=1
result2=1
for k in range(len(co)):
    result*=co[k]
    result2*=co2[k]
print(int(result2/result))
