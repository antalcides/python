#!/usr/bin/env python
import numpy as np
import pylab as plt
import scipy

#Generar datos de entrada
xdata=np.linspace(-4,+4,40)
ydata=np.sin(2*xdata+0.5)

#Graficar datos de entrada
plt.plot(xdata,ydata,'ks',ms=10) #grafico

x=np.linspace(-3.9,+3.9,100)
y=np.array([])
for i in range(len(x)):
 dist=x[i]-xdata
 print x[i]
 #print dist
 xsup=np.max(xdata[dist>=0])
 xinf=np.min(xdata[dist<0])  
 print xinf, xsup
 ysup=ydata[xdata==xsup]
 yinf=ydata[xdata==xinf]
 
 m=(ysup-yinf)/(xsup-xinf)
 b=yinf-m*xinf
 y=np.append(y,m*x[i]+b)
  #ind_sup=np.min(indices[dist>=0])
#  ind_sup=np.argmin(dist[dist>=0])
#  xsup=xdata[ind_sup]
#  ysup=ydata[ind_sup]
#  ind_inf=np.argmax(dist[dist<0])
#  xinf=xdata[ind_inf]
#  yinf=ydata[ind_inf]

plt.plot(x,y,'ro',ms=3) 
plt.show()


