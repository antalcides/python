#! /usr/bin/env python
# Este es un archivo en donde guardamos funciones

# Librerias necesarias para esta libreria
from math import *
from numpy import *
from scipy import *
from pylab import *

# Definicion de funciones
# En este ejemplo se ponen dos rutinas para integrar numericamente una funcion

def euler(x_inicio,t_inicial,t_final,delta_t,mi_funcion):
    # La funcion toma punto inicial, timepo inicial y final de integracion,
    # delta t o paso de integracion, cadena de caracter de la funcion a integrar 
    # Definicion de variables locales
    x0 = x_inicio
    t0 = t_inicial
    dt = delta_t    
    t = t0
    x = x0
    time=[]
    sol=[]
    # Algoritmo de integracion con Euler
    while (t < t_final):
        time.append(t)
        sol.append(x)
        x = x + (dt*mi_funcion(x))
        t = t + dt
    # Se regresa como solucion en dos listas el tiempo y la solucion numerica
    return [time,sol]


def rk(x_inicio,t_inicial,t_final,delta_t,mi_funcion):
    # La funcion toma punto inicial, timepo inicial y final de integracion,
    # delta t o paso de integracion, cadena de caracter de la funcion a integrar 
    # Definicion de variables locales
    x0 = x_inicio
    t0 = t_inicial
    dt = delta_t
    t = t0
    x = x0
    time=[]
    sol=[]    
    # Algoritmo de integracion con Runge Kutta de 4to orden
    while (t < t_final):
        time.append(t)
        sol.append(x)
        # Algoritmo Runge-Kutta cuarto orden
        k1 = dt*mi_funcion(x)
        k2 = dt*mi_funcion(x + 0.5*k1)
        k3 = dt*mi_funcion(x + 0.5*k2)
        k4 = dt*mi_funcion(x + 1.0*k3)
        # Siguiente paso de tiempo
        x = x + (1./6.)*(k1 + 2.*k2 + 2.*k3 + k4)
        t = t + dt
    # Se regresa como solucion en dos listas el tiempo y la solucion numerica
    return [time,sol]

