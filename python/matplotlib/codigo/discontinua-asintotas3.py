#/usr/bin/env python3
# -*- coding: utf-8 -*-
 
 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save
 
f = lambda x: pow(x, 2) / (pow(x, 2) - x - 6)
 
 
fig, ax = plt.subplots(figsize=(7, 6))
x = np.linspace(-9.0, 9, 1000)
pos = np.where(np.abs(np.diff(f(x))) >= 10.0)[0]
x = np.insert(x, pos, np.nan)
ax.axis([x[0], x[-1], -9.5, 9.5])
ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')
ax.spines['left']
ax.spines['bottom']
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ticks = []
for i in range(-9, 9, 1):
    ticks.append(i)
ticks.remove(0)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.plot(x, f(x), color='b', linestyle='-', lw=1.5)
#ax.plot(x, x + 1.0, color='r', linestyle='--', lw=2.0)
ax.axhline(y=1.0, xmin=-9.0, xmax=9.0, linewidth=2.0,
           color='g', linestyle='--')
ax.axvline(x=3.0, ymin=-9.0, ymax=9.0, linewidth=2.0,
           color='brown', linestyle='--')
ax.axvline(x=-3.0, ymin=-9.0, ymax=9.0, linewidth=2.0,
           color='brown', linestyle='--')
ax.legend([r'$f(x)=\frac{x^2}{x^2-x-6}$', r'$y=1$', r'$x=-3$', r'$x=3$'], loc='lower right')
ax.annotate(r'$X$', xy=(9., 0.75), size=16, color='black')
ax.annotate(r'$Y$', xy=(0.25, 9.0), size=16, color='black')
ax.annotate(r'$x = 3$', xy=(1, 5), size=16, color='brown')
ax.annotate(r'$x = -3$', xy=(-5.5, 5), size= 16, color='brown')
ax.annotate(r'$y = 1$', xy=(1, 1.5), size= 16, color='g')
ax.set_title(r'$Funci\'on\; Discontinua$', fontsize=18)
ax.grid('on')
plt.savefig('figsize.pdf')
plt.show()
tikz_save( 'figsize.tikz' );
