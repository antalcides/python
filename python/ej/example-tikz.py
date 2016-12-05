# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 18:38:47 2014

@author: antalcides
"""

from numpy import arange
from matplotlib2tikz import save as tikz_save
import matplotlib.pyplot as plt

x = arange(0,10,0.5)
fig = plt.figure(figsize=(2, 2))
plt.plot(x,x**2)
plt.title("A lovely plot")
plt.ylabel("$y=x^2$")
plt.xlabel("La parábola ")
tikz_save( 'figsize.tikz' );
plt.savefig('figsize.pdf')