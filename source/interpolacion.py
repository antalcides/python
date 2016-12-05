# interpolacion.py
#
# Implementacion de los siguientes metodos de interpolacion:
#
# 1. Interpolacion directa
# 2. Polinomio de Lagrange
# 3. Polinomio de Newton
# 4. Metodo de Newton-Gregory
# 5. Splines cubicos

from pylab import *

def interDirecta(x,f,*arg):
   # c = interDirecta(x,f)
   # yt,c = interDirecta(x,f,xt)
   #
   # Se implementa el metodo de interpolacion directa con los datos x y f para
   # el polinomio:
   #
   #    Pn(x) = c[0] x**n + c[1] x**(n-1) + c[2] x**(n-2) + ... + c[n-1]x + c[n]
   #
   # En caso de proporcionarse un arreglo xt de datos de prueba, se evalua el
   # polinomio y se produce el arreglo yt:
   #
   #    yt[i] = Pn(x[i])
   
   n = len(f)-1
   A = ones([n+1,n+1])
   for i in range(n+1):
      for j in range(n):
         A[i,j] = x[i]**(n-j)

   c = solve(A,f)

   if len(arg)>=1:
      xt = arg[0]
      yt = []
      for t in range(len(xt)):
         suma = c[n]
         for i in range(n):
            suma += c[i]*xt[t]**(n-i)
         yt = yt + [suma]

      return yt,c
   else:
      return c


def Lagrange(x,f,xt):
   # yt,c = Lagrange(x,f,xt)
   #
   # Se implementa el polinomio de interpolacion de Lagrange con los datos x y f.
   # Se evalua el polinomio de interpolacion y se produce el arreglo yt:

   n = len(f)-1
   yt = []
   for t in range(len(xt)):
      suma = 0
      for i in range(n+1):
         prod = 1.0
         for j in range(n+1):
            if j!=i:
               prod *= (xt[t]-x[j])/(x[i]-x[j])
         suma  += f[i]*prod
      yt += [suma]
   return yt



def Newton(x,f,xt):
   # yt = Newton(x,f,xt)
   #
   # Se realiza la interpolacion mediante el polinomio de Newton para los
   # valores xt.
   
   # Se obtiene la matriz de diferencias divididas D
   n = len(f)-1
   D = zeros([n+1,n+1])
   D[:,0] = f
   for j in range(1,n+1):
      for i in range(n-j+1):
         D[i,j] = (D[i+1,j-1]-D[i,j-1])/(x[i+j]-x[i])
   # Se realiza la interpolacion para los valores de prueba xt
   yt = []
   for t in range(len(xt)):
      sum = 0
      for i in range(n+1):
         prod = 1.0
         for j in range(i):
            prod *= xt[t]-x[j]
         sum += D[0,i]*prod
      yt += [sum]
   return yt


def combinaciones(s,k):
   # Regresa las combinaciones de s tomando k, donde s puede ser no entera
   # (Esta funcion es necesaria para el metodo de Newton-Gregory.)
   res = 1.0
   if k!=0:
      for i in range(1,k+1):
         res *= (s-i+1)/i
   return res

def NewtonGregory(x1,deltaX,f,xt):
   # yt = NewtonGregory(x1,deltaX,f,xt)
   #
   # Metodo de interpolacion Newton-Gregory para datos uniformemente
   # espaciados
   #     x1: primer dato
   # deltaX: espaciamiento de los datos (x(i+1)-x(i))
   #      f: vector de valores de y
   #     xt: valores para interpolar

   # Se obtiene la matriz de diferencias deltaF
   n = len(f)-1
   deltaF = zeros([n+1,n+1])
   deltaF[:,0] = f
   for j in range(1,n+1):
      for i in range(n-j+1):
         deltaF[i,j] = deltaF[i+1,j-1]-deltaF[i,j-1]
   deltaF = deltaF[0:n,1:n+1]

   # Se encuentra el vector de indices no enteros s
   s = (xt-x1)/deltaX

   # Se realiza la interpolacion para los valores de prueba xt
   yt = []
   for t in range(len(xt)):
      sum = f[0]
      for i in range(n):
         sum += combinaciones(s[t],i+1)*deltaF[0,i]
      yt += [sum]
   return yt

def SplineCubico(*args):
   #    [yt,coef] = SplineCubico(x,f,xt)    (1)
   #           yt = SplineCubico(xt,x,coef) (2) 
   #         coef = SplineCubico(x,f)       (3)
   #
   # Realiza interpolacion mediante splines cubicos.
   
   xt = []
   coef = []
   if len(args)==3:
      if len(args[0])==len(args[1]):
         caso = 1
         x = args[0]
         f = args[1]
         xt = args[2]
      else:
         caso = 2
         xt = args[0]
         x = args[1]
         coef = args[2]
         a = coef[0]
         b = coef[1]
         c = coef[2]
         d = coef[3]
   elif len(args)==2:
      caso = 3
      x = args[0]
      f = args[1]
   
   n = len(x)-1

   if caso==1 or caso==3:
      # Formar matriz A y vector bb
      A = zeros([n+1,n+1])
      bb = zeros([n+1,1])
      A[0,0] = 1.
      h = x[1:n+1]-x[0:n]
      for i in range(1,n):
         A[i,i-1:i+2] = array([h[i-1],2*(h[i-1]+h[i]),h[i]])
         bb[i] = (3./h[i])*(f[i+1]-f[i])-(3./h[i-1])*(f[i]-f[i-1])
      A[n,n] = 1.

      # Resolver sistema A*b = bb
      b = solve(A,bb)
      
      # Obtener a, b, y d
      c = zeros([n,1])
      a = zeros([n,1])
      for i in range(n):
         c[i] = (1./h[i])*(f[i+1]-f[i])-(h[i]/3.)*(b[i+1]+2*b[i])
         a[i] = 1./(3.*h[i])*(b[i+1]-b[i])
      d = reshape(f[0:n],(n,1))
      b = b[0:n]
      # Formar el arreglo coef que contiene todos los coeficientes
      coef = array([a,b,c,d]) 

   if caso==1 or caso==2:
      # Interpolar para los valores de prueba
      yt = []
      for t in range(len(xt)):
         # Encontrar cual segmento usar
         i = find(x<=xt[t])
         if len(i)==0:
            i = 0;
         elif len(i)>=1:
            i = i[-1]
         if i>=n:
            i = n-1;
         # Evaluar el spline
         yt += [a[i,0]*(xt[t]-x[i])**3+b[i,0]*(xt[t]-x[i])**2+\
                c[i,0]*(xt[t]-x[i])+d[i,0]]

   # Dependiendo del caso, regresar yt y/o coef
   if caso==1:
      return  yt,coef
   elif caso==2:
      return yt
   elif caso==3:
      return coef




if __name__ == '__main__':
##    x = array([0.4,2.5,4.3,5.0,6.0])
##    f = array([1.00,0.50,2.00,2.55,4.00])
##    
    x = array([0,1,2,3,4])
    f = array([0.2231,0.6065,1.0000,0.6065,0.2231])
    xt = linspace(-1,5,200)
    [yt,coef] = SplineCubico(x,f,xt)
    plot(x,f,'ok',xt,yt,'b')
    axis((-1,5,-0.5,1.5))
    xlabel('x')
    ylabel('y')
    title('interpolacion usando splines cubicos')
    legend(('datos','splines'),'best')
    grid()
    show()
    print coef
    
