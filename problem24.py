"""
Problema que calcula las permitaciones y muestra la última
"""
import numpy as np
import math
import sys
from itertools import permutations
from time import time

tiempo_inicial=time()

lista=list(permutations([0,1,2,3,4,5,6,7,8,9]))
print(lista[999999])

tiempo_final=time()
tiempo_ejecucion=tiempo_final-tiempo_inicial
print(tiempo_ejecucion)
