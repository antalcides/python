from pylab import *

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
   while t<=tf:
      k1 = h*f(t,y)
      k2 = h*f(t+0.5*h,y+0.5*k1)
      k3 = h*f(t+0.5*h,y+0.5*k2)
      k4 = h*f(t+h,y+k3)
      y += (k1+2*k2+2*k3+k4)/6.0
      t += h
      Y = concatenate((Y,reshape(y,(1,n))))
      T = concatenate((T,[t]),1)
   return T,Y

def tierra(t,x):
    m = 5.97219E24
    M = 1.98855E30
    G = 6.67384E-11
    d = sqrt(x[0]**2+x[1]**2)
    F = G*m*M/d**2
    theta = arctan2(x[1],x[0])
    Fx = -F*cos(theta)
    Fy = -F*sin(theta)
    f = x.copy()
    f[0] = f[2]
    f[1] = f[3]
    f[2] = Fx/m
    f[3] = Fy/m
    return f

anio = 365.*24*60*60
h = anio/20.
r = 150E9
v0 = 30E3
x0 = array([r,0.,0.,v0])
T,Y = RungeKutta4(tierra,h,x0,0.,1*anio) 
plot(Y[:,0],Y[:,1])
k = 1.5
axis((-k*r,k*r,-k*r,k*r))
grid()
show()
   
