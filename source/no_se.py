# 1. Que hace esta funcion?
# 2. Como funciona?
# 3. Rastree el programa insertando instrucciones
#    print para observar el contenido de las variables
#    durante la ejecucion.

def no_se(n):
   # n debe ser un entero positivo
   if n<1 or n==1:
      return []
   lista = [2]
   for i in range(3,n+1):
      i_si_es = True
      for j in lista:
         if i%j == 0:
            i_si_es = False
            break
      if i_si_es:
         lista = lista + [i]
   return lista


