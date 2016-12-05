from numpy import *

def EGaussiana(A,*arg):
# Implementacion del metodo de eliminacion gaussiana para resolver
# sistemas de ecuaciones lineales y encontrar la inversa de una matriz.
#
#    Inv, det = EGaussiana(A)
#
# Regresa Inv, la inversa de A, y el determinante de A.
#
#    x, det = EGaussiana(A,b)
#
# Regresa x, la solucion del sistema Ax=b, y el determinante de A.

# 1 marzo 2012
# Manuel Valenzuela

   n,m = A.shape
   if len(arg) >= 1:      # Solucion de sistema de ecuaciones
      A = concatenate((A,arg[0]),axis=1)
   elif n==m:             # Inversa de matriz
      A = concatenate((A,eye(n)),axis=1)
   det = 1.0

   for i in range(n):
      # Encontrar pivote maximo
      k = i
      for j in range(i+1,n):
         if abs(A[j,i]) > abs(A[k,i]):
            k = j

      # Intercambiar renglones
      if k!=i:
         A[i,:], A[k,:] = A[k,:].copy(), A[i,:].copy()
         det *= -1


      # Hacer ceros en la columna i debajo del renglon i
      for j in range(i+1,n):
         A[j,:] -= A[i,:]*A[j,i]/A[i,i]

   for i in range(n-1,-1,-1):
      # Hacer uno el elemento i,i
      det *= A[i,i]
      A[i,:] /= A[i,i]
      
      # Hacer ceros en la columna i arriba del renglon i
      for j in range(i-1,-1,-1):
         A[j,:] -= A[i,:]*A[j,i]


   return A[:,n:],det


