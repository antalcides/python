from matplotlib.pyplot import *
from numpy import *
from mpl_toolkits.axes_grid.axislines import SubplotZero 
 
X = linspace(0,10,25)
Y = linspace(-5,5,25)
x, y = meshgrid(X,Y)
 
fig = figure(figsize=(10,6))
ax = SubplotZero(fig,111)
fig.add_subplot(ax)
for direction in ["xzero","yzero"]:
	ax.axis[direction].set_visible(True)
	ax.axis[direction].set_axisline_style("->")
for direction in ["top","bottom","left","right"]:
	ax.axis[direction].set_visible(False)
ax.axis["yzero"].set_axis_direction("left")
ax.grid(True)
ax.minorticks_on()
 
ax.contour(x,y, x**2 + 2.*x*y +y**2 - 8.*x, [0],linewidths=1.5,colors='r')
ax.text(1.75,-4.5,r'$x^2+2xy+y^2-8x=0$',color='r')
ax.arrow(.5,-1,0,5,color='orange',head_width=.1,head_length=.2)
ax.text(.75,4,r'$\bar{y}$',color='orange')
ax.arrow(-2.5,1.5,5.5,0,color='orange',head_width=.1,head_length=.2)
ax.text(3,1,r'$\bar{x}$',color='orange')
ax.plot(.5,1.5,'ko')
ax.text(.25,1.75,r'V')
 
ax.arrow(-4.5,-4.5,9,9,color='m',ls='dashed',lw=.5), ax.text(-4,-4,r'$x=y$',color='m')
ax.arrow(-5.5,-4.5,9,9,color='grey',ls='dashed',lw=.5), ax.text(-6,-3,r'$x=y-1$',color='grey')
ax.arrow(-2,-1,5,5,color='g',head_width=.2,head_length=.2), ax.text(2.9,4.2,r'$y$',color='g')
ax.arrow(-4.5,4.5,9,-9,color='c',ls='dashed',lw=.5), ax.text(-4,4,r'$x=-y$',color='c')
ax.arrow(-2.5,4.5,9,-9,color='b',ls='dashed',lw=.5), ax.text(-2,4,r'$x=y+2$',color='b')
ax.arrow(-1,3,4,-4,color='g',head_width=.2,head_length=.2), ax.text(2.5,-1,r'$x$',color='g')
 
ax.plot([0,1,2],[0,1,2],'ko')
ax.text(.1,.1,r'A'), ax.text(1.1,1,r'M'), ax.text(1.9,2.1,r'B')
 
#ax.text(10,.1,"x")
#ax.text(.1,5,"y")
xticks(arange(-6,11,1))
yticks(arange(-5,6,1))
ax.set_ylim(-5,5)
ax.set_xlim(-6,10)
show()
fig.savefig("Test.svg",bbox_inches="tight",\
        pad_inches=.15)
