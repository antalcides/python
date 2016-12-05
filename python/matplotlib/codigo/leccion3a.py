#! /usr/bin/env python
#Uso de librerias en Python

# Libreria de funciones matematicas
from math import *
# Libreria para utilizar arreglos tipicos de algebra lineal
from numpy import *
# Libreria de funciones que se utilizan en computo cientifico
from scipy import *
# Libreria de funciones para generar graficas
from pylab import *

# En muchas ocasiones en ligar de manejar listas como si fuesen vectores.
# Con la libreria de numpy es mucho mas facil manejar los arreglos
# Comando para generar un arreglo mas eficiente
a=array([[2,3],[3,4]])
print a
b=array([[1,2],[3,4]])
print b
# La forma para llamar a los elementos del arreglo es similar al de las listas pero 
# con mayor familiaridad
print "Elemento de b",b[1,1]
print "------------"
# La multiplicacion se hace componente a componente
print a*b
# Multiplicacion usual de matrices
print mat(a)*mat(b)
print mat(a)*mat(a)
print "------------"

# Se pueden crear arreglos con intervalos con numeros reales
# Con arange se hace un arreglo (inicio,final,paso)
tiempo = arange(0,1.,0.1)
print tiempo
# Hay numeros muy utilies que estan bien definidos como pi
print pi
#
# Otra forma de generar un arreglo es con linspace. Es parecido a arange, pero
# se especifica (inicio,fin,numero de pasos)
tiempo = linspace(0.,5*pi,100)
print tiempo

print "------------"
# Con los arreglos anteriores se puede evaluar funciones facilmente
evaluar = sin(tiempo)
print evaluar
# Con el siguiente comando de hace la grafica de la funcion. Se pueden poner varias graficas en
# el mismo espacio con el formato (x1,y1,x2,y2,...)
plot(tiempo,evaluar)
# Mostrar la grafica
show()

