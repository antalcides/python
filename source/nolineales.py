from pylab import *

def Bisecciones(f,x1,x2,tol=0.0001):
   # Encuentra una raiz de la funcion f en el intervalo (x1,x2)
   # mediante bisecciones sucesivas
   while True:
      x = (x1+x2)/2.0
      if f(x1)*f(x)<0:
         x2 = x
      else:
         x1 = x
      if abs((x1-x2)/x)<tol or \
         abs(f(x))<tol:
         break
   return x


def NewtonRaphson(f,fp,x,tol=0.0001):
   # Encuentra una raiz de la funcion f tomando x como punto inicial
   # mediante el metodo de Newton-Raphson
   while True:
      xAnt = x
      x = x - f(x)/fp(x)
      print x
      #print '%f %f %f' % (x,f(x),fp(x))
      if abs((x-xAnt)/x)<tol or abs(f(x))<tol:
         break
   return x


def Secante(f,xt,xtmenos,tol=0.0001):
   # Encuentra una raiz de la funcion f tomando x como punto inicial
   # y xAnt como el punto anterior, mediante el metodo de la secante
   while True:
      fxt = f(xt)
      xtmas = xt - fxt*(xt-xtmenos)/(fxt-fxtmenos)
      if abs((xtmas-xt)/xt)<tol or abs(fxt)==0:
         break
      xtmenos = xt
      xt = xtmas
      fxtmenos = fxt
   return xtmas


def NewtonRaphson2(f,g,fx,fy,gx,gy,x,y,tol=0.0001):
   # Implementacion del metodo de Newton-Raphson para la
   # solucion de un sistema de 2 ecuaciones lineales con dos
   # incognitas
   
   while True:
      # Se crea el sistema de ecuaciones para encontrar
      # delta x, delta y
      A = matrix([[fx(x,y),fy(x,y)],[gx(x,y),gy(x,y)]])
      b = matrix([[-f(x,y)],[-g(x,y)]])
      deltas = solve(A,b)
   

      # Se incrementan los valores de x y
      x += deltas[0,0]
      y += deltas[1,0]
      print 'x=%12.9f y=%12.9f' % (x,y)

      # Si ya se encontro la raiz, se termina el ciclo
      if abs(f(x,y))<tol and abs(g(x,y))<tol:
         return (x,y)


def NewtonRaphsonV(F,NablaF,x,tol=0.0001):
   # Implementacion del metodo de Newton-Raphson para la
   # solucion de un sistema de n ecuaciones lineales con n
   # incognitas

   while True:
      # Se crea el sistema de ecuaciones para encontrar
      # delta x
      A = NablaF(x)
      b = -F(x)
      delta = solve(A,b)
   

      # Se incrementan los valores de x
      x += delta

      # Si ya se encontro la raiz, se termina el ciclo
      if abs(max(F(x)))<tol:
         return x

   



if (__name__ == '__main__'):
   def fcn(x):
      return 3*x + sin(x) - exp(x) 


   def fcnp(x):
      return 3 + cos(x) - exp(x)

   def f(x,y):
      return x**2 + y**2 - 1

   def g(x,y):
      return x - y

   def fx(x,y):
      return 2*x

   def fy(x,y):
      return 2*y

   def gx(x,y):
      return 1.

   def gy(x,y):
      return -1.

   def F(x):
      x1 = x[0,0]
      x2 = x[1,0]
      return matrix([[x1**2+x2**2-1],[x1-x2]])

   def NablaF(x):
      x1 = x[0,0]
      x2 = x[1,0]
      return matrix([[2*x1,2*x2],[1.,-1.]])


   x = linspace(0,2,101)
   y = map(fcn,x)
   plot(x,y)
   grid()
   show()

   rb = Bisecciones(fcn,1.5,2.)
   print 'Raiz encontrada por bisecciones    = %f\n' % rb

   rn = NewtonRaphson(fcn,fcnp,1.)
   print 'Raiz encontrada por Newton-Raphson = %f\n' % rn

   rs = Secante(fcn,1.,0.)
   print 'Raiz encontrada por Secante        = %f\n' % rs


   (rx,ry) = NewtonRaphson2(f,g,fx,fy,gx,gy,2.,1.)
   print 'Raiz encontrada por Newton-Raphson x=%f y=%f' % (rx,ry)

   x0 = matrix([[2.],[1.]])
   r = NewtonRaphsonV(F,NablaF,x0)
   print 'Raiz encontrada por Newton-Raphson:'
   for i in range(len(r)):
      print 'x%d= %f' % (i,r[i])

   
