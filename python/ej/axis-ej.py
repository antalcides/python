#/usr/bin/env python3
# -*- coding: utf-8 -*-
 
 
import numpy as np
from matplotlib import * 
import matplotlib.pyplot as plt
def seq(start, stop, step=1):
    n = int(round((stop - start)/float(step)))
    if n > 1:
        return([start + step*i for i in range(n+1)])
    else:
        return([])
 
def f(x):
    return np.piecewise(x, [x < 2.0, x > 2.0], [lambda x: x ** 2.0, lambda x: 4.0])
 
 
fig, ax = plt.subplots()
x = np.linspace(-5.0, 5.0, 1000)
a =seq(-5, 6., 0.5)
ax.axis([x[0], x[-1], x[0], x[-1]])
ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')
ax.spines['left']
ax.spines['bottom']
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ticks = []
#for i in range(int(a[0]), int(a[-1] + 0.5), 1):
for i in np.arange(-5, 5, 0.5): 
    ticks.append(i)
ticks.remove(0)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.plot(x, f(x), 'b-', 2, 4, 'wo', markeredgecolor='b',
        markerfacecolor='w', lw=2.0)
ax.legend([r'$f(x)$'], loc='lower right')
ax.set_title(r'$Funci\'on\; A\; Trozos$')
ax.grid('on')
plt.show()
