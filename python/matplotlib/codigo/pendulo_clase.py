#!/usr/bin/env python
import scipy
import numpy as np
import pylab as plt

def F(t,theta,vtheta):
  return vtheta

def G(t,theta,vtheta,g=9.8,l=1.):
  return -(g/l)*np.sin(theta)

def euler_step(h,ti,thetai,vthetai,FF,GG):
  thetai_mas_1=thetai+h*FF(ti,thetai,vthetai)
  vi_mas_1=vthetai+h*GG(ti,thetai,vthetai)

  return (thetai_mas_1,vi_mas_1)

def midpt_step(h,ti,thetai,vthetai,FF,GG):
  k1=h*FF(ti,thetai,vthetai)
  l1=h*GG(ti,thetai,vthetai)
  k2=h*FF(ti+h/2.,thetai+k1/2.,vthetai+l1/2.)
  l2=h*GG(ti+h/2.,thetai+k1/2.,vthetai+l1/2.)
  thetai_mas_1=thetai+k2
  vi_mas_1=vthetai+l2
 
  return (thetai_mas_1,vi_mas_1) 

def leapfrog_step(h,ti,thetai,vthetai,F,G):

  vthetai_plus_half=vthetai+(h/2.)*G(ti,thetai,vthetai)
  thetai_plus_1=thetai+h*F(ti,thetai,vthetai_plus_half)
  vthetai_plus_1=vthetai_plus_half + (h/2.)*G(ti,thetai_plus_1,vthetai_plus_half)

  return (thetai_plus_1,vthetai_plus_1)

t_o,theta_o,v_o=0.,10.*np.pi/180.,0.
t_f=12.
Npasos=800.
h=(t_f-t_o)/Npasos
 
for theta_o in np.array([10.,45.,120.,179.])*np.pi/180.:  
   #Sacar las cuentas
   t,theta=np.array([t_o]),np.array([theta_o])
   v=np.array([v_o])
   for n in np.arange(Npasos):
     t_new=t[-1]+h
   #  theta_new,v_new=euler_step(h,t[-1],theta[-1],v[-1],F,G) 
     theta_new,v_new=midpt_step(h,t[-1],theta[-1],v[-1],F,G)
   #  theta_new,v_new=leapfrog_step(h,t[-1],theta[-1],v[-1],F,G)
   
     t=np.append(t,t_new)
     theta=np.append(theta,theta_new)
     v=np.append(v,v_new)
   
   #Graficar
   plt.subplot(131)
   plt.plot(t,theta)
   plt.xlabel('t')
   plt.ylabel('$\\theta$')
   plt.subplot(132)
   plt.plot(theta,v)
   plt.xlabel('$\\theta$')
   plt.ylabel('$v_\\theta$')
   plt.subplot(133)
   g,l=9.8,1.
   E=0.5*(v**2) + g*(l-l*np.cos(theta))
   plt.plot(t,E)
   plt.xlabel('t')
   plt.ylabel('E(t)')

plt.show()
