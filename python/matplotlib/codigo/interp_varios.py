#!/usr/bin/env python
import numpy as np
import pylab as plt
import scipy
import scipy.interpolate

def my_sin(x):
  return np.sin(2*x+0.5)

def my_rational(x):
 return 1./(1.+x**2)
  

my_func=my_rational
   
#Generar datos de entrada
xdata=np.linspace(-4.,+4,10)
ydata=my_func(xdata)

#Ordenar en orden creciente
sorted_ind=xdata.argsort()
xdata=xdata[sorted_ind]
ydata=ydata[sorted_ind]

#Graficar datos de entrada
plt.plot(xdata,ydata,'ks',ms=10) #grafico

x=np.linspace(-3.9,+3.9,100)
yfunc=my_func(x)
plt.plot(x,yfunc,'k-',lw=2)

#Interpolacion Lineal
IntLineal=scipy.interpolate.interp1d(xdata,ydata,kind='linear')
plt.plot(x,IntLineal(x),'ro',ms=4)

#Polinomio de Lagrange
Lagrange=scipy.interpolate.lagrange(xdata,ydata)
plt.plot(x,Lagrange(x),'bo',ms=4)

#Cubic Spline
cs_order=3
CSpline=scipy.interpolate.UnivariateSpline(xdata,ydata,k=cs_order,s=0)
plt.plot(x,CSpline(x),'o',color='orange',ms=5)
titulo="El cubic spline es de orden k=%4d" % (cs_order)
plt.title(titulo)
plt.show()
