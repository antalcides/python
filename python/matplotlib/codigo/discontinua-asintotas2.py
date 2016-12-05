#/usr/bin/env python3
# -*- coding: utf-8 -*-
 
 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save
 
f = lambda x: pow(x, 3) / (pow(x, 2) - x - 6)
 
 
fig, ax = plt.subplots()
x = np.linspace(-15.0, 15.0, 1000)
pos = np.where(np.abs(np.diff(f(x))) >= 10.0)[0]
x = np.insert(x, pos, np.nan)
ax.axis([x[0], x[-1], -15.5, 15.5])
ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')
ax.spines['left']
ax.spines['bottom']
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ticks = []
for i in range(-15, 16, 5):
    ticks.append(i)
ticks.remove(0)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.plot(x, f(x), color='b', linestyle='-', lw=1.5)
ax.plot(x, x + 1.0, color='r', linestyle='--', lw=2.0)
ax.axvline(x=-2.0, ymin=-15.0, ymax=15.0, linewidth=2.0,
           color='g', linestyle='--')
ax.axvline(x=3.0, ymin=-15.0, ymax=15.0, linewidth=2.0,
           color='brown', linestyle='--')
ax.legend([r'$f(x)=\frac{x^3}{x^2-x-6}$', r'$y=x+1$', r'$x=-2$', r'$x=3$'], loc='lower right')
ax.annotate(r'$OX$', xy=(13.5, 0.75), size=16, color='black')
ax.annotate(r'$OY$', xy=(0.25, 14.0), size=16, color='black')
ax.annotate(r'$x = 3$', xy=(3.25, 1), size=16, color='brown')
ax.annotate(r'$x = -2$', xy=(-6.4, 1), size= 16, color='g')
ax.annotate(r'$y = x + 1$', xy=(-12, -5), rotation=34, size=16, color='r')
ax.set_title(r'$Funci\'on\; Discontinua$', fontsize=18)
ax.grid('on')
plt.savefig('figsize8.pdf')
plt.show()
tikz_save( 'figsize8.tikz' );
