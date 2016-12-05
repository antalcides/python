#/usr/bin/env python3
# -*- coding: utf-8 -*-
 
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import MaxNLocator
matplotlib.colors.ColorConverter.colors['mc1'] = (0.,0.69,0.92)
matplotlib.colors.ColorConverter.colors['mc2'] = (0.83,0.93,0.99)
def seq(start, stop, step=1):
    n = int(round((stop - start)/float(step)))
    if n > 1:
        return([start + step*i for i in range(n+1)])
    else:
        return([]) 
 
f = lambda x: np.sin(1/x)
 
 
fig, ax = plt.subplots()
x = np.linspace(-2.0, 2.2, 1000)
pos = np.where(np.abs(np.diff(f(x))) >= 10.0)[0]
x = np.insert(x, pos, np.nan)
a =seq(-2, 2.5, 0.2)
ax.axis([a[0], a[-1], -2.5, 2.5])
ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')
ax.spines['left']
ax.spines['bottom']
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ticks = []
for i in np.arange(-2, 2, 0.5):
    ticks.append(i)
ticks.remove(0)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
###################################
al = 7 # arrow length in points
arrowprops=dict(clip_on=False, # plotting outside axes on purpose
     frac=1., # make end arrowhead the whole size of arrow
     headwidth=al, # in points
     facecolor='k')
kwargs = dict(  
                  xycoords='axes fraction',
                  textcoords='offset points',
                  arrowprops= arrowprops,
               )
  
ax.annotate("",(1,0.5),xytext=(-al,0), **kwargs) # bottom spine arrow
ax.annotate("",(0.5,1),xytext=(0,-al), **kwargs) # left spin arrow
##======================= left arrow axis
ax.annotate("",
            xy=(-2.0021, 0), xycoords='data',
            xytext=(0, 0), textcoords='data',size=20,
            va="center", ha="center",
            arrowprops=dict(arrowstyle="-|>",
                            connectionstyle="arc3",fc="black"), 
                                        )  
                                        ###========================
ax.annotate("",
            xy=(0, -1.3033854), xycoords='data',
            xytext=(0, 0), textcoords='data',size=20,
            va="center", ha="center",
            arrowprops=dict(arrowstyle="-|>",
                            connectionstyle="arc3",fc="black"), 
                                        )                                                                      
#======================================
#-- Decorate the spins
#arrow_length = 20 # In points

# X-axis arrow

####################################
ax.plot(x, f(x), color='mc1', linestyle='-', lw=1.5)
ax.legend([r'$f(x)=\sin(\frac{1}{x})$'], loc='lower right')
ax.annotate(r'$X$', xy=(1.8, 0.05), size=16, color='black')
ax.annotate(r'$Y$', xy=(0.05, 1.2), size=16, color='black')
ax.set_title(r'$Funci\'on\; Discontinua$', fontsize=18)
plt.gca().xaxis.set_major_locator(MaxNLocator(prune='both'))

ax.grid('on')
xlim(-2,2)
ylim(-1.3,1.3)
plt.show()
