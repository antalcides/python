#*********************************************
#series.py
#Autor: SymPy Project
#Modificadores
#Carlos José Grajeda C. 
#Aldo Francisco Rojas
#Hugo Oliveros
#15 de Noviembre del 2009
#Este programa es una muestra de derivar en
#SymPy
#Fecha última de actualización: 15 Noviembre 2009
#*********************************************

from sympy import *
from sympy import Symbol, cos
x = Symbol('x')
e = 1/cos(x)
print "La función es: ", e
print "La serie es: ", e.series(x, 0, 10)

print "La integral de e es: ", integrate(e,x)
print "La integral de x**2 +2*x es: ", integrate(x**2 +2*x, x)
