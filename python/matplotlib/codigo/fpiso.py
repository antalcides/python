#/usr/bin/env python3
# -*- coding: utf-8 -*-
 
 
import numpy as np
import matplotlib.pyplot as plt
 
 
fig, ax = plt.subplots()
x = np.linspace(-6.0, 6.0, 1000)
pos = np.where(np.abs(np.diff(np.floor(x))) >= 1.0)[0] + 1
x = np.insert(x, pos, np.nan)
ax.axis([x[0] - 0.5, x[-1] + 0.5, x[0] - 0.5, x[-1] + 0.5])
ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')
ax.spines['left']
ax.spines['bottom']
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ticks = []
for i in range(int(x[0]), int(x[-1] + 1), 1):
    ticks.append(i)
ticks.remove(0)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.plot(x, np.floor(x), color='b', linestyle='-', lw=2.0)
igual = np.arange(-6, 6, 1)
igual_mas_uno = igual + np.ones(12, np.int)
ax.plot(igual, igual, 'bo', markeredgecolor='b', markerfacecolor='b',
        lw=2.0,  label='_nolegend_')
ax.plot(igual_mas_uno, igual, 'bo', markeredgecolor='b', markerfacecolor='w',
        lw=2.0,  label='_nolegend_')
ax.legend([r'$f(x)=\lfloor x \rfloor$'], loc='lower right')
ax.annotate(r'$OX$', xy=(x[-1] - .5, 0.25), size=16, color='black')
ax.annotate(r'$OY$', xy=(0.25, x[-1]), size=16, color='black')
ax.set_title(r'$Funci\'on\; Piso$', fontsize=18)
ax.grid('on')
plt.show()
