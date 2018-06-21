import time
start = time.time()
p1=1
p2=2
p5=5
p10=10
p20=20
p50=50
E1=100
E2=200
suma=0
total=0

for a in range(201):
    suma=a*p1
    if suma<=200:
        for b in range(101):
            suma=a*p1+b*p2
            if suma<=200:
                for c in range(41):
                    suma=a*p1+b*p2+c*p5
                    if suma<=200:
                        for d in range(21):
                            suma=a*p1+b*p2+c*p5+d*p10
                            if suma<=200:
                                for e in range(11):
                                    suma=a*p1+b*p2+c*p5+d*p10+e*p20
                                    if suma<=200:
                                        for f in range(5):
                                            suma=a*p1+b*p2+c*p5+d*p10+e*p20+f*p50
                                            if suma<=200:
                                                for g in range(3):
                                                    suma=a*p1+b*p2+c*p5+d*p10+e*p20+f*p50+g*E1
                                                    if suma<=200:
                                                        for h in range(2):
                                                            suma=a*p1+b*p2+c*p5+d*p10+e*p20+f*p50+g*E1+h*E2
                                                            if suma==200:
                                                                total+=1

print(total)
elapsed = time.time() - start
print(elapsed)
