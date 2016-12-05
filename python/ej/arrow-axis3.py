import pylab as p
import numpy as n

from mpl_toolkits.axes_grid import axislines


def cubic(x) :
    return x**3 + 6*x


def set_axes():
    fig = p.figure(1)
    ax = axislines.SubplotZero(fig, 111)
    fig.add_subplot(ax)

    for direction in [ 'xzero', 'yzero']:
        ax.axis[direction].set_axisline_style('->', size=2)
        ax.axis[direction].set_visible(True)
               
    for direction in [ 'xzero', 'yzero']:
        ax.axis[direction].set_axisline_style('<-', size=2)
        ax.axis[direction].set_visible(True)

    for direction in ['right', 'top', 'left', 'bottom']:
        ax.axis[direction].set_visible(False)

    ax.axis['xzero'].set_label('X')
    ax.axis['yzero'].set_label('Y')

    ax.axis['yzero'].major_ticklabels.set_axis_direction('right')
    ax.axis['yzero'].set_axislabel_direction('+')
    ax.axis['yzero'].label.set_rotation(-90)
    ax.axis['yzero'].label.set_va('center')


set_axes()

X = n.linspace(-15,15,100)
Y = cubic(X)

p.plot(X, Y)

p.xlim(-5.0, 5.0)
p.ylim(-15.0, 15.0)

p.xticks(n.linspace(-5, 5, 11, endpoint=True))
p.grid(True)

p.show()
