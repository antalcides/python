#/usr/bin/env python3
# -*- coding: utf-8 -*-
 
 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
 
 
f = lambda x: np.sin(1/x)
 
 
fig, ax = plt.subplots()
x = np.linspace(-2.5, 2.5, 1000)
pos = np.where(np.abs(np.diff(f(x))) >= 10.0)[0]
x = np.insert(x, pos, np.nan)
#ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.axis([x[0], x[-1], -2.5, 2.5])
ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')
ax.spines['left']
ax.spines['bottom']
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ticks = []
for i in range(-2, 2, 1):
    ticks.append(i)
ticks.remove(0)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.plot(x, f(x), color='b', linestyle='-', lw=1.5)
ax.set_ylim(-1.2,1.2)
#ax.plot(x, x + 1.0, color='r', linestyle='--', lw=2.0)
#ax.axvline(x=-2.0, ymin=-15.0, ymax=15.0, linewidth=2.0,
          # color='g', linestyle='--')
#ax.axvline(x=3.0, ymin=-15.0, ymax=15.0, linewidth=2.0,
           #color='brown', linestyle='--')
ax.legend([r'$f(x)=\sin\left(\frac{1}{x}\right)$ '], loc='lower right')
ax.annotate(r'$X$', xy=(2.3, 0.01), size=16, color='black')
ax.annotate(r'$Y$', xy=(0.01, 1.1), size=16, color='black')
#ax.annotate(r'$x = 3$', xy=(3.25, 1), size=16, color='brown')
#ax.annotate(r'$x = -2$', xy=(-4.5, 1), size= 16, color='g')
#ax.annotate(r'$y = x + 1$', xy=(-10, -5), rotation=35, size=16, color='r')
ax.set_title(r'$Funci\'on\; Discontinua$', fontsize=18)
ax.grid('on')
plt.show()
