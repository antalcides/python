# Example/template of plot of one variable, f=f(x), saving to a (PNG) file.
# Look at MatPlotLib documentation for more details about 'plot' :
# http://matplotlib.sourceforge.net/users/pyplot_tutorial.html
# Author : Roberto Colistete Jr.
#
# NumPy and MatPlotLib are loaded :
from pylab import *
##############################################################################
# Personalize your plot parameters here.
# x values from xi to xf with numx points being sampled :
xi = 0.0; xf = 10.0; numx = 150
# y = f(x), just change the expression after 'return' :
def f(x):
     return 2.5*exp(-1.0*x/2)*cos(pi*x)
# Line style. First letter is color : r (red), g (green), b (blue), k (black), etc.
# Then the line style : '-' (solid), '--' (dashed), '-.' (dash-dot), ':' (dotted).
linecolorstyle='b-'
# Line width in points :
linewidthpt = 2.0
# Labels for x and y axis, here including TeX expressions (inside '$') :
xlabeltext = r'$t\,(s)$'; ylabeltext = r'$x\,(m)$'
# Plot title, here including TeX expressions (inside '$') :
titletext = r'Damped harmonic oscillator : $m=1.0$, $b=1.0$, $x_0=2.5$, $\omega=\pi$'
# Option (True/False) to show a grid of dashed lines :
gridflag = True
# Name of the file where the plot is saved (in current directory).
# Possible extensions : png, pdf, ps, eps and svg :
plotfilename = 'plotfx.png'
##############################################################################
# Don't change the code below 
x = arange(xi, xf, (xf-xi)/(numx-1))
y = f(x)
plot(x, y, linecolorstyle, linewidth=linewidthpt)
xlabel(xlabeltext); ylabel(ylabeltext); title(titletext)
grid(gridflag)
# To show instead of saving the plot, just use 'show()'.
savefig(plotfilename)
