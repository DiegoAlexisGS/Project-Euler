"""
¿Cuántas rutas existen en un retícula de 20x20?
"""
import numpy as np
import time
tam=21
rutas=np.zeros((tam,tam))
start = time.time()
rutas[0][0]=0
for i in range(tam):
    for j in range(tam):
        if i==0 and j>0:
            rutas[i][j]=1
        if i>0 and j==0:
            rutas[i][j]=1
        if i>0 and j>0:
            rutas[i][j]=rutas[i-1][j]+rutas[i][j-1]
elapsed = time.time() - start
print(rutas[tam-1][tam-1])
print(elapsed)
