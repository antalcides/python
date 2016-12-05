c     Programa para aplicar el metodo de Euler o EDO's
c     como ejempo usaremos la EDO's:
c                 dy/dx = sqrt(x**2+y**2)
c                  y(2)= 0.5
      program Euler
      real x(1), y(1), h
      Integer i,n,res
             res =1
20    if (res.eq.1)then

c     Definamos condiciones iniciales
      x(1)=0.0
      y(1)=0.5
c     Valor a calcular: y(2.3)
c     Definamos para la iteración, donde es el numero de item.
      print*, 'Introduzca el valor del numero de iteraciones'
      read*, n
      h=(0.1-0.0)/n
       print*, 'El valor aproximado de la funcion es'
c Ciclo para la iteracion:
      do 10 i=1,n+1
      x(i+1)= x(i)+h
      y(i+1)=y(i)+h*(sqrt(x(i)**2+y(i)**2))

      print*, x(i),y(i)

      open(10,file='Eulernew.txt',status='old')
         write (10,200) 'Las coordenadas son ' ,x(i) , y(i)
200      format(a20,d8.3,d8.3)

10    continue

        print*, 'Si quiere continuar digite 1 si no cero'
       read*,  res
       goto 20
       endif

      end

