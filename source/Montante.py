from numpy import *

def Montante(A,*arg):
# Implementacion del metodo Montante para resolver sistemas de
# ecuaciones lineales y encontrar la inversa de una matriz.
#
#    Inv, det = Montante(A)
#
# Regresa Inv, la inversa de A, y el determinante de A.
#
#    x, det = Montante(A,b)
#
# Regresa x, la solucion del sistema Ax=b, y el determinante de A.

# 8 marzo 2011
# Manuel Valenzuela

   n,m = A.shape
   if len(arg) >= 1:      # Solucion de sistema de ecuaciones
      A = concatenate((A,arg[0]),axis=1)
   elif n==m:             # Inversa de matriz
      A = concatenate((A,eye(n)),axis=1)

   det = 1.
   pivAnt = 1.

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
         
      piv = A[i,i]
      # Hacer ceros en la columna del pivote
      for j in range(n):
         if j!=i:
            A[j,:] = (A[j,:]*piv - A[i,:]*A[j,i])/pivAnt

      # Guardar el pivote anterior
      pivAnt = piv

   # Dividir entre el pivote
   A /= piv

   # Obtener el determinante
   det *= piv
   return A[:,n:],det




   
