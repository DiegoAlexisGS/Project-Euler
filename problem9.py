

for i in range(1000):
    if i>0:
        for j in range(1000):
            if i<j:
                for m in range(1000):
                    if j<m:
                        if i+j+m==1000 and i**2+j**2==m**2:
                            print(i," ",j," ",m)
                            print(i*j*m)
