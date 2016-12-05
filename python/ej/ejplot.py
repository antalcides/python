#!/usr/bin/env python

from pylab import *
import matplotlib 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
matplotlib.colors.ColorConverter.colors['mc1'] = (0.,0.69,0.92)
matplotlib.colors.ColorConverter.colors['mc2'] = (0.83,0.93,0.99)

t = arange(-6.0, 4.0, 0.001)
s=np.sin(1/t) 

ax = subplot(111)
ax.plot(t, s,'r-',color="mc1")
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.set_xlim(-2,2)
ax.set_ylim(-1.2,1.20)
#plt.gca().xaxis.set_major_locator(MaxNLocator(prune='lower'))
text(1.9, 0.1, r'X')
text(0.1, 1.1, r'Y')

#text(-3.5, 12,
    # r"$f(x)=\frac{X^3}{4}+\frac{3.X^2}{4}-\frac{3.X}{2}-2$", 
     #horizontalalignment='center',
     #fontsize=17)

plt.savefig('latexetmatplotlib.png')
show()
