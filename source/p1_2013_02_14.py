# Problema 1: for, range
print '\nProblema 1_1'
A = 5
for r in range(3,8,2):
   A = A + r
print A

   
# Problema 2: for, range
print '\nProblema 2_1'
suma = 0
for n in range(1,4):
   suma = suma + n**n
print suma


# Problema 3: if, elif, else
print '\nProblema 3_1'
x = 5
w = 10
y = w * 2.4
if (y > 30) or (w != 10):
   x = x - 5
elif (y < 30) and (w != 10):
   x = x + 5
else:
   x = x*5
print x

# Problema 4: if, elif, else
print '\nProblema 4_1'
a = 5
b = 10
if ((a*b/2 < a*a) and (b != a)):
   print "Cerrado"
elif (a*b/2 == a*a):
   print "Activo, %d, %d" % (a, b)
else:
   print "Inactivo, %d, %d" % (b, a)



# Problema 5: funciones
print '\nProblema 5_1'
def fib(f1,f2):
   return f1 + f2
print fib(1, fib(1,1))
##Opciones:
   


print '#####################################################################'


print '\nProblema 1_2'
A = 4
for r in range(2,8,2):
   A = A + r
print A

# Problema 2: for, range
print '\nProblema 2_2'
suma = 1
for n in range(1,4):
   suma = suma + n**n
print suma

# Problema 3: if, elif, else
print '\nProblema 3_2'
x = 4
w = 10
y = w * 2.4
if (y > 30) or (w != 10):
   x = x - 5
elif (y < 30) and (w != 10):
   x = x + 5
else:
   x = x*5
print x

# Problema 4: if, elif, else
print '\nProblema 4_2'
a = 5
b = 10
if ((a*b/2 < a*a) and (b != a)):
   print "Cerrado"
elif (a*b/2 == a*a):
   print "Activo, %d, %d" % (a, b)
else:
   print "Inactivo, %d, %d" % (b, a)


# Problema 5: funciones
print '\nProblema 5_3'
def fib(f1,f2):
   return f1 + f2
print fib(2, fib(1,1))


print '#####################################################################'


# Problema A
print '\nProblema A'
def facto(n):
   i = 1
   if n==0:
      prod = 1
   else:
      prod = 1
      while i<=n:
         prod = prod*i
         i = i + 1
   return prod
print facto(4)

# Problema B
print '\nProblema B_1'
def f1(x):
   if x>0:
      return x**2
   else:
      return -x**2

def f2(x):
   s = 1
   while x>-3 and x<2:
      s = 2*s+x
      x = x - 1
   return s

for i in range(-3,3):
   if i%2==0:
      print 'f1=', f1(i)
   else:
      print 'f2=', f2(i)

# Problema B
print '\nProblema B_2'
def f1(x):
   if x>0:
      return x**2
   else:
      return -x**2

def f2(x):
   s = 1
   while x>-3 and x<2:
      s = 2*s+x
      x = x - 1
   return s

for i in range(-3,3):
   if i%2==0:
      print 'f2=', f2(i)
   else:
      print 'f1=', f1(i)


# Problema C
print '\nProblema C_1'
def eleva(B,m):
   lista = []
   for i in range(1,m+1):
      lista = lista + [B**i]
   return lista
print eleva(2,4)

# Problema C
print '\nProblema C_2'
def eleva(B,m):
   lista = []
   for i in range(1,m+1):
      lista = lista + [1./B**i]
   return lista
print eleva(2,4)

