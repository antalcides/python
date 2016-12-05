#*********************************************
#gr�fica.py
#Autor: SymPy Project
#Modificadores
#Carlos Jos� Grajeda C. 
#Aldo Francisco Rojas
#Hugo Oliveros
#11 de Noviembre del 2009
#Este programa grafica en 
#SymPy
#Fecha �ltima de actualizaci�n: 12 Noviembre 2009
#*********************************************

from sympy import *
x,y = symbols('xy')
Plot(cos(x*3)*cos(y*5)-y)

x = symbols("x")
Plot(x**2+2*x**15)

x,y = symbols("xy")
Plot(x**2*7*y**3)
