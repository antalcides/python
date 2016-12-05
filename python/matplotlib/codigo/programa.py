#!/usr/bin/env python

import numpy as np
import scipy
import pylab as plt

filename='pop_5000Ma.dat'
datos=scipy.genfromtxt(filename,comments='#')
#Temp,Lum=scipy.genfromtxt(filename,comments='#',usecols=(2,3),unpack=True) #esto lee solo las columnas 

Temp=datos[:,2] #Guardar la tercera columna en variable Temp
Lum=datos[:,3]
Masa=datos[:,0]

#Crear objeto figura donde se hara el grafico (ventana). 
fig=plt.figure(1,figsize=(12,7))
#Agregar un sub-grafico. 122= hacer una fila de graficos con dos columnas, graficar en el 1er subplot (izquierda)
ax=fig.add_subplot(121)
#Grafico log-log. El argument 'k.' significa usar puntos (.) negros (k)
ax.loglog(Temp,Lum,'k.')
#Fijar los limites del eje x e invertirlo
ax.set_xlim(1.e4,1.e3)
#Etiquetas de los ejes
ax.set_xlabel('Temperatura (K)')
ax.set_ylabel('$L_V (L_\odot)$')
#
#Agregar otro sub-grafico. Igual al anterior pero ahora graficar en el 2do grafico (derecha)
ax2=fig.add_subplot(122)
#Grafico de logL vs logT donde cada punto tienen un color proporcional a su masa
col=ax2.scatter(np.log10(Temp),np.log10(Lum),c=Masa)
#Etiquetas de los ejes
ax2.set_xlabel('$\log(T[K])$')
ax2.set_ylabel('$\log(L_V/L_\odot)$')
#Limites del eje x e invertir
ax2.set_xlim(4,3)
#Anadir la barra de colores correspondiente al grafico ax2.scatter
axcb=plt.colorbar(col,ax=ax2,aspect=30)
#Etiqueta de la barra de colores
axcb.set_label('Masa ($M_\odot$)')
#Guardar la figura en foramto png
plt.savefig('mifigura.png')
plt.show()

