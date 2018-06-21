"""
y"=p(x)y'+q(x)y+r(x)
"""
import sympy as sp
import numpy as np


def metlindiffin(a,b,al,be,N):
    #paso1
    h=(b-a)/(N+1)
    x=a+h
    a=np.zeros[N+1]
    b=np.zeros[N+1]
    d=np.zeros[N+1]
    l=np.zeros[N+1]
    u=np.zeros[N+1]
    z=np.zeros[N+1]
    w=np.zeros[N+2]
    a[0]=2+h**2*q(x)
    b[0]=-1+(h/2)*p(x)
    d[0]=-h**2*r(x)+(1+(h/2)*p(x))*al
    #paso2
    for i in range(1,N-1):
        x=a+i*h
        a[i]=2+h**2*q(x)
        b[i]=-1+(h/2)*p(x)
        c[i]=-1-(h/2)*p(x)
        d[i]=-h**2*r(x)
    #paso3
    x=b-h
    a[N]=2+h**2*q(x)
    c[N]=-1-(h/2)*p(x)
    d[N]=-h**2*r(x)+(1-(h/2)*p(x))*be
    #Los siguientes pasos resuelven un sistema lineal tridiagonal con un algoritmo
    #Paso4
    l[0]=a[0]
    u[0]=b[0]/a[0]
    z[0]=d[0]/l[0]
    #Paso5
    for j in range(1,N-1):
        l[j]=a[j]-c[j]*u[j-1]
        u[j]=b[j]/l[j]
        z[j]=(d[j]-c[j]*z[j-1])/l[j]
    #Paso6
    l[N]=a[N]-c[N]*u[N-1]
    z[N]=(d[N]-c[N]*z[N-1])/l[N]
    w[0]=al
    w[N+1]=be
    w[N]=z[N]
    for k in range(N-1,1):
        w[k]=z[k]-u[k]*w[k+1]
    for m in range(N+1):
        x=a+mh
        print(x,w[m])

metlindiffin(1,10,1,2,10)
