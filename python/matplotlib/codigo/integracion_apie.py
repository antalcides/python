#!/usr/bin/env python

import numpy as np
import scipy.integrate

#--------------------------
def trap(x,f,h):
  
  Int=0
  for i in np.arange(1,len(x)-1,1):
	Int=f[i]+Int

  Int=(f[0]+f[-1])/2.+Int
  Int=h*Int 
  
  return Int
#-----------------------

def trap2(x,f,h):

 Int=h*np.sum(f[1:-1])+h*(f[0]+f[-1])/2.   
 return Int 
 
def super_trap(x,f):
 hf=0.5*(x[1:]-x[0:-1])*(f[0:-1]+f[1:])
 return np.sum(hf)

def simp_un_tercio(f,h):
 h=h/2. 
#                 --fi---  --fi+1-- --fi+2--
 return np.sum((h/3.)*(f[0:-2]+4.*f[1:-1]+f[2:]))

def cuadratura_gauss_chimba(func):
  Igauss=func(-1./np.sqrt(3.)) + func(+1/np.sqrt(3.))
  return Igauss

def cuadratura_gauss_gral(func,a,b):
  mu_o,mu_1=-1./np.sqrt(3.),+1/np.sqrt(3.)
  x_o=0.5*((b-a)*mu_o+(b+a))
  x_1=0.5*((b-a)*mu_1+(b+a))
  I=0.5*(b-a)*(func(x_o)+func(x_1))
  return I

def my_func(x):
 return np.exp(x)

#-------------------------
  
h=0.00001
xdata=np.arange(0,3.+h,h)
f=xdata
  
print len(xdata)
  
I=trap(xdata,f,h)
print I
I2=trap2(xdata,f,h)
print I2
Igen=super_trap(xdata,f)
print Igen
Ipy=scipy.integrate.trapz(f,x=xdata)
print Ipy

Isimp=simp_un_tercio(f,h)
print 'Isimp=',Isimp
Is=scipy.integrate.simps(f,dx=h)
print Is

Igauss=cuadratura_gauss_gral(my_func,0.,+1)
print 'Igauss=',Igauss,(np.exp(1)-1)
