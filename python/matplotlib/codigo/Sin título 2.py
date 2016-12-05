# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 11:41:09 2014

@author: antalcides
"""

import numpy as np
import matplotlib.pyplot as plt
#-----------------------------------------------------------------------------
fig, ax = plt.subplots()
N = 101
xx = np.linspace(0, 100, N)
yy = np.linspace(0, 100, N) + 15 * np.random.rand(N)
ax.scatter(xx, yy, marker='x')
ax.grid(True)
#-----------------------------------------------------------------------------
from matplotlib2tikz import save as tikz_save
tikz_save('learn_mpl2tikz.tex',
        figureheight = '\\figureheight',
        figurewidth = '\\figurewidth')
plt.show()