
def factoriales():
   n = input('dame un entero: ')
   while n>0:
      print '%3d! = %d = %7.2e' % (n,factRec(n),factRec(n))
      n = input('dame un entero: ')


   

def factRec(n):
   if n==0:
      return 1
   else:
      return n*factRec(n-1)
