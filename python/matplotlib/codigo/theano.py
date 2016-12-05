#!/usr/bin/python
 
from matplotlib import rc
from pylab import *
from theano import *
import theano.tensor as T
import numpy
 
rc('text', usetex=True)
rc('font', family='serif')
 
x = T.fvector('x')
x1 = T.fscalar('x1')
y = 1/(1 + T.exp(-x))
y1 = 1/(1 + T.exp(-x1))
logistic = function([x], y)
logistic1 = function([x1], y1)
grady = T.grad(y1, x1)
derivada = function([x1], grady)
 
a = float(input('Introduce el extremo izqdo. \n'))
b = float(input('Introduce el extremo drcho. \n'))
particion = float(input('Introduce la longitud de particion del intervalo. \n'))
pderiv = float(input('Introduce el punto donde hallar su recta tangente. \n'))
 
xval = arange(a,b,particion, dtype='float32')
z,w,w1=T.fscalars('z', 'w', 'w1')
rectatg2 = (x-z)*w+w1
rectatg3 = function([x, Param(z, default=pderiv), Param(w, default=derivada(pderiv)), Param(w1, default=logistic1(pderiv))], rectatg2)
 
figure(1)
 
plot(xval, logistic(xval), linewidth=1.5, color='r')
plot(xval, rectatg3(xval), linewidth=1.0, color='g')
ylim([0,1])
 
xlabel(r'\textbf{Abcisa}', fontsize=12)
ylabel(r'\textit{Ordenada}',fontsize=12)
title(r"Funcion logistica f(x) = $\displaystyle\frac{1}{1+e^{-x}}$", fontsize=12, color='r')
legend(('Funcion Logistica', 'Recta Tangente'),'upper left', shadow=True, fancybox=True)
 
leg = gca().get_legend()
ltext  = leg.get_texts()
llines = leg.get_lines()
frame  = leg.get_frame()
 
frame.set_facecolor('0.80')
setp(ltext, fontsize='small')
setp(llines, linewidth=1.5)
 
grid(True)
axhline(linewidth=1.5, color='b')
axvline(linewidth=1.5, color='b')
 
figure(2)
 
plot(xval, logistic(xval), 'k.')
plot(xval, rectatg3(xval), linewidth=1.0, color='g')
ylim([0,1])
legend(('Funcion Logistica', 'Recta Tangente'),'upper left', shadow=True, fancybox=True)
leg = gca().get_legend()
ltext  = leg.get_texts()
llines = leg.get_lines()
frame  = leg.get_frame()
 
frame.set_facecolor('0.80')
setp(ltext, fontsize='small')
setp(llines, linewidth=1.5)
 
xlabel(r'\textbf{Abcisa}', fontsize=12)
ylabel(r'\textit{Ordenada}',fontsize=12)
title(r"Funcion logistica f(x) = $\displaystyle\frac{1}{1+e^{-x}}$", fontsize=12, color='r')
grid(True)
axhline(linewidth=1.5, color='r')
axvline(linewidth=1.5, color='r')
 
figure(1)
savefig('fig1')
figure(2)
savefig('fig2')
 
show()
