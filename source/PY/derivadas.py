#*********************************************
#derivadas.py
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
x,y = symbols('xy')
f = x**2 / y + 2 * x - ln(y)
print "La función a derivar: ", f
print "Esta es la primera derivada: ", diff(f,x)
print "Esta es la derivada de f, respecto de y: ", diff(f,y)
print "Esta es la derivada de otra derivada, respecto de y: ", diff(diff(f,x),y)
