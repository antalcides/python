## Example/template of surface plot of two variables, f=f(x,y).
## The surface plot can have orientation, color maps, color bar, etc, and 
## be saved to a (PNG) file.
## Look at MatPlotLib documentation for more details about 'plot_surface' :
## http://matplotlib.sourceforge.net/mpl_toolkits/mplot3d/tutorial.html#surface-plots
## Author : Roberto Colistete Jr.
#
## NumPy and MatPlotLib are loaded :
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
##############################################################################
## Personalize your plot parameters here.
## x values from xi to xf with numx points being sampled :
xi = -2.0; xf = 2.0; numx = 60
## y values from yi to yf with numy points being sampled :
yi = -2.0; yf = 2.0; numy = 60
## z = f(x,y), just change the expression after 'return' :
def f(x,y):
     return (cos(pi*x*y)**2)*exp(-(x**2+y**2)/2)
## Surface 3D orientation in azimuth and elevation(degree units). 
## Use 'None' for the default 
surfaceazim = None
surfaceelev = None
#surfaceazim = 120
#surfaceelev = 40
## Line width in points, 0.0 to make the lines invisible over the surface :
linewidthpt = 0.0
## Option (True/False) to use color map :
surfacecolormapflag = True
## If 'surfacecolormapflag' is True, then color map (type after 'cm.') can be 
## jet, gray, binary, spectral, hsv, hot, cool, cooper, bone, autumn, winter, 
## summer, spring, etc. Look at : 
## http://www.scipy.org/Cookbook/Matplotlib/Show_colormaps 
# surfacecolormap = cm.gray
surfacecolormap = cm.jet
## If 'surfacecolormapflag' is False then the same color will be used for all 
## vectors. Color : r (red), g (green), b (blue), k (black), etc.
surfacesamecolor = 'r'
## Option (True/False) to show color bar of the surface plot :
surfacebarflag = False
## Labels for x and y axis :
xlabeltext = r'x'; ylabeltext = r'y'
## Plot title, here including TeX expressions (inside '$') :
titletext = r'$f(x,y)=\,\cos(\pi\,x\,y)^2 e^{-\frac{x^2+y^2}{2}}$'
## Name of the file where the plot is saved (in current directory).
## Possible extensions : png, pdf, ps, eps and svg :
plotfilename = 'surfacefxy.png'
##############################################################################
# Don't change the code below
fig = plt.figure()
if  (surfaceazim == None) or (surfaceelev== None):
    ax = fig.add_subplot(111, projection='3d')
else:
    ax = fig.add_subplot(111, projection='3d', azim = surfaceazim, elev = surfaceelev)
x = arange(xi, xf, (xf-xi)/(numx-1))
y = arange(yi, yf, (yf-yi)/(numy-1))
X,Y = meshgrid(x, y)
Z = f(X,Y)
if surfacecolormapflag:
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=surfacecolormap, \
                           linewidth=linewidthpt, antialiased=True)
else:
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, color=surfacesamecolor, \
                           linewidth=linewidthpt, antialiased=True)
if surfacebarflag:
    ax.w_zaxis.set_major_locator(LinearLocator(10))
    ax.w_zaxis.set_major_formatter(FormatStrFormatter('%.03f'))
    fig.colorbar(surf, shrink=0.5, aspect=6)
xlabel(xlabeltext); ylabel(ylabeltext); title(titletext)
## To show instead of saving the plot, just use 'show()' :
#show()
savefig(plotfilename)

