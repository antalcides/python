# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 11:28:29 2014

@author: antalcides
"""

from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0,10,.1)
y = np.sin(x)
plt.plot(x,y)
ax = plt.gca()
ax.axhline(.4, xmin=0, xmax=1, linewidth=0.3, color=(0, 0, 0, 0.75))
plt.show()