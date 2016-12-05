# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 19:01:39 2014

@author: antalcides
"""
#!/usr/bin/env python
#coding:utf-8

import numpy


class Senl:
    '''
    Clase que define un sistema de ecuaciones no lineales y diferentes
    metodos para hallar su solucion
    '''
    def __init__(self):
        pass

    def newton(self,paso,numero):
        return 0

    def llamada_funcion(self,x,a):
        resultado=self.funcion(x,a)
        return numpy.array(resultado)

    def jacobiano(self,x,a,tol=0.001):
        res=[]
        xtemp=numpy.array(x)

        x1=xtemp.copy()
        for i in range(len(x1)):
            x2=x1.copy()
            x2[i]+=tol
            r=(self.llamada_funcion(x2,a)-self.llamada_funcion(x1,a))/tol
            res.append(r)

        jac=numpy.array(res[0])
        for i in range(len(res)-1):
            jac=numpy.vstack((jac,numpy.array(res[i+1])))

        return jac.transpose()

    def solver_newton(self,x0,a,max_iter=50,tol=0.0001):
        x1=numpy.array(x0)
        e=1.0
        iteracion=0

        while iteracion < max_iter and e > tol:
            A=self.jacobiano(x1,a)
            B=self.llamada_funcion(x1,a)
            res=numpy.linalg.solve(A,B)
            x1=x1-res
            e1=abs(res.max())
            e2=abs(res.min())
            e=max([e1,e2])
            print("error: ", e)
            print( "Nº iteracion: ",iteracion)
            iteracion+=1
        return x1

if __name__ == '__main__':
    def f(x,a):
        r=[0.0]*2

        r[0]=x[0]*x[1]-a[0]
        r[1]=x[0]+x[1]-a[1]

        return r

    def drag(x,a):
        '''
        funcion para determinar el coeficiente de rodadura de un coche
        x[0] sera el coeficiente de rodadura
        a[0] sera el producto del coeficiente aerodinamico por la superficie
        frontal
        a[1] sera la velocidad maxima del coche
        a[2] sera la masa del coche
        a[3] sera la potencia maxima del coche
        '''
        r=[0.0]*2
        rho=1.204

        r[0]=0.5*rho*a[0]*a[1]**3+x[0]*a[2]*9.81*a[1]-a[3]
        r[1]=x[1]-x[0]
        return r

    sistema=Senl()
    sistema.funcion=drag

    print( sistema.solver_newton(x0=[1.0,0.0],a=[0.61,56.67,1340.0,90000.0]))
