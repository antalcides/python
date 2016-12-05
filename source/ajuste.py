from pylab import *
# Implementacion de metodos de minimos cuadrados para ajuste a polinomios
# y exponenciales. Se ajustan datos de la forma (x,f) donde x y f deben ser
# de tipo array.
#
# 15 marzo 2012
# Manuel Valenzuela

def ajustePolinomio(x,f,n,*arg):
# Ajusta los datos (x,f) a un polinomio de la forma
# a0 x^n + a1 x^(n-1) + ... an x^n + a(n+1)
#
#    a = ajustePolinomio(x,f,n)
#    yt, a = ajustePolinomio(x,f,n,xt)
#
# Regresa los coeficientes a. Si se proporciona xt, evalua
# el polinomio y regresa yt.
   N = len(x)
   A = zeros([n+1,n+1])
   A[0,0] = N
   for j in range(1,n+1):
      A[0,j] = sum(x**j)
      
   for i in range(1,n+1):
      A[i,0:n] = A[i-1,1:n+1]
      A[i,n] = sum(x**(n+i))

   c = zeros([n+1,1])
   for i in range(n+1):
      c[i,0] = sum(x**i*f)
      
   coef = solve(A,c)
   a = coef[::-1]

   if len(arg)>=1:
      yt = []
      xt = arg[0]
      for t in range(len(xt)):
         suma = a[n,0]
         for i in range(n):
            suma += a[i,0]*xt[t]**(n-i)
         yt += [suma]
      return yt, a
   else:
      return a


def ajusteExp(x,f,*arg):
# Ajusta los datos (x,f) a una curva exponencial de la forma
# f(x) = a*exp(b*x)
#
#  a,b = ajusteExp(x,f)
#  yt,a,b = ajusteExp(x,f,xt)
#
# Regresa los coeficientes a y b. Si se proporciona xt, evalua
# el f y regresa yt.

   A = matrix([[len(x),sum(x)],[sum(x),sum(x**2)]])
   bb = matrix([[sum(log(f))],[sum(x*log(f))]])
   c = solve(A,bb)
   a = exp(c[0,0])
   b = c[1,0]

   if len(arg)>=1:
      xt = arg[0]
      yt = a*exp(b*xt)
      return yt,a,b
   else:
      return a,b


def ajusteAXB(x,f,*arg):
# Ajusta los datos (x,f) a una curva exponencial de la forma
# f(x) = a*x^b.
#
#  a,b = ajusteAXB(x,f)
#  yt,a,b = ajusteAXB(x,f,xt)
#
# Regresa los coeficientes a y b. Si se proporciona xt, evalua
# el f y regresa yt.
   A = matrix([[len(x),sum(log(x))],[sum(log(x)),sum(log(x)**2)]])
   bb = matrix([[sum(log(f))],[sum(log(x)*log(f))]])
   c = solve(A,bb)
   a = exp(c[0,0])
   b = c[1,0]

   if len(arg)>=1:
      xt = arg[0]
      yt = a*xt**b
      return yt,a,b
   else:
      return a,b


if (__name__ == '__main__'):
   x = array([0.4,2.5,4.3,5.0,6.0],float)
   f = array([1.00,0.50,2.00,2.55,4.00],float)
   xt = linspace(0,6,101)
   ft1,a1 = ajustePolinomio(x,f,1,xt)
   ft2,a2 = ajustePolinomio(x,f,2,xt)
   ft3,a3 = ajustePolinomio(x,f,3,xt)
   plot(xt,ft1,'b',xt,ft2,'r',xt,ft3,'g',x,f,'ok')
   xlabel('x')
   ylabel('y')
   title('Ajuste a polinomios')
   legend(('0.5301x+0.0803','0.1981x^2-0.7153x+1.2095',
           '-0.0198x^3+0.3909x^2-1.2081x+1.4171'),'best')
   show()
   print 'a:',a1.transpose()
   print 'a:',a2.transpose()
   print 'a:',a3.transpose()
