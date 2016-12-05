from pylab import *

def Euler(f,h,y0,t0,tf):
   # [T,Y] = Euler(f,h,y0,t0,tf)
   #
   # Metodo de Euler para resolver una ecuacion diferencial
   # ordinaria de la forma:
   #
   #   dy
   #   -- = f(t,y)  con condicion incial y(t0) = y0
   #   dt

   t = t0
   n = size(y0)
   y = y0
   Y = reshape(y,(1,n))
   T = [t]
   while t<tf:
      y += h*f(t,y)
      t += h
      Y = concatenate((Y,reshape(y,(1,n))))
      T = concatenate((T,[t]),1)
   return T,Y


def EulerM(f,h,y0,t0,tf):
   # [T,Y] = dEulerM(f,h,y0,t0,tf)
   #
   # Metodo de Euler modificado para resolver una ecuacion diferencial
   # ordinaria de la forma:
   #
   #   dy
   #   -- = f(t,y)  con condicion inicial y(t0) = y0
   #   dt

   t = t0
   n = si.ze(y0)
   y = y0
   Y = reshape(y,(1,n))
   T = [t]
   while t<tf:
      yh = y + h*f(t,y)
      y += (h/2.)*(f(t,y)+f(t+h,yh))
      t += h   
      Y = concatenate((Y,reshape(y,(1,n))))
      T = concatenate((T,[t]),1)
   return T,Y


def RungeKutta4(f,h,y0,t0,tf):
   # T,Y = RungeKutta4(f,h,y0,t0,tf) 
   #
   # Metodo Runge-Kutta de cuarto orden para resolver una ecuacion 
   # diferencial ordinaria de la forma:
   #
   #   dy
   #   -- = f(t,y)  con condicion inicial y(t0) = y0
   #   dt


   t = t0
   n = size(y0)
   y = y0
   Y = reshape(y,(1,n))
   T = [t]
   while t<tf:
      k1 = h*f(t,y)
      k2 = h*f(t+0.5*h,y+0.5*k1)
      k3 = h*f(t+0.5*h,y+0.5*k2)
      k4 = h*f(t+h,y+k3)
      y += (k1+2*k2+2*k3+k4)/6.0
      t += h
      Y = concatenate((Y,reshape(y,(1,n))))
      T = concatenate((T,[t]),1)
   return T,Y

