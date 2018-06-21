import numpy as np
vector=np.arange(1000)+1
suma=0
for i in range(len(vector)):
    suma+=(i+1)**(i+1)
print(suma)
for j in range(10):
    print(str(suma)[j-10])
