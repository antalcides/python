#/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy.solvers import *
from sympy import *
from matplotlib import rcParams


# Activating LateX
rcParams['text.latex.unicode'] = True
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = '\\usepackage{amsthm}', '\\usepackage{amsmath}', '\\usepackage{amssymb}',
'\\usepackage{amsfonts}', '\\usepackage[T1]{fontenc}', '\\usepackage[utf8]{inputenc}'

# Declaring the three planes as functions
f1 = lambda x, y: (-x + 2 * y) / 2.
f2 = lambda x, y: -2 * x + y
f3 = lambda x, y: -x + y

# Declaring symbolic variables
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

# Solving the linear system
fun1 = x -2*y + 2*z
fun2 = 2*x - y + z
fun3 = x - y + z
solucion = solve([fun1, fun2, fun3], [x, y, z])

# Printing the solution
pprint(('Solución Del Sistema es: {}').format(solucion))


# Stablishing our ranges for our variables
x1 = y1 = np.arange(-6, 6, 0.25)
ceros = np.zeros(len(x1))

# Stablishing our meshgrid
x, y = np.meshgrid(x1, y1)

# Our 3D Canvas Figure Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting the solution
ax.plot(ceros, y1, zs=y1, zdir='z', color='#6F0382', linewidth=2.5)

# Plotting the 3 planes
ax.plot_surface(x, y, f1(x, y), rstride=1, cstride=1, linewidth=0, antialiased=True, color='blue')
ax.plot_surface(x, y, f2(x, y), rstride=1, cstride=1, linewidth=0, antialiased=True, color='red')
ax.plot_surface(x, y, f3(x, y), rstride=1, cstride=1, linewidth=0, antialiased=True, color='green')

# Putting the limits in the axes
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-15, 15)

# Writing the axis labels
ax.set_xlabel('x', color='blue')
ax.set_ylabel('y', color='blue')
ax.set_zlabel('z', color='blue')

# Writing The Title of The Plot
ax.set_title(r'$Graphical\; Resolution\; Linear\; System\; 3 \times 3$', fontsize=18)

# Stablishing the plots of our legend labels
blue_proxy = plt.Rectangle((0, 0), 1, 1, fc='b')
red_proxy = plt.Rectangle((0, 0), 1, 1, fc='r')
green_proxy = plt.Rectangle((0, 0), 1, 1, fc='g')
purple_proxy = plt.Rectangle((0, 0), 1, 1, fc='#6F0382')

# Drawing Our Legend
ax.legend([blue_proxy,red_proxy, green_proxy, purple_proxy], [r'$x-2y+2z=0$',r'$2x-y+z=0$', r'$x-y+z=0$', r'$Sol.\; (0,\lambda, \lambda)$'], loc='upper left')

plt.show()
