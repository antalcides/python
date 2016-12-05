import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.axislines import SubplotZero

def mplot(sage_plot, equal_scale = False, edit_res = False):
    """
    This function convert sage_plot, created at sage, in matplotlib graph.
    """
    plt.clf()
    fig = plt.figure()
    ax = SubplotZero(fig, 111)
    fig.add_subplot(ax)
    L = sage_plot.matplotlib().gca().lines
    for t in L:
        data = t.get_data()
        ax.add_line(mpl.lines.Line2D(data[0], data[1]))
    ax.autoscale_view()
    if equal_scale:
        ax.axis('equal')
    for direction in ["xzero", "yzero"]:
        ax.axis[direction].set_axisline_style("-|>", size = 2)
        ax.axis[direction].set_visible(True)
    for direction in ["left", "right", "bottom", "top"]:
        ax.axis[direction].set_visible(False)
    ax.axis["yzero"].set_axis_direction("left")
    ax.minorticks_on()    
    ax.grid()
    if edit_res:
        return(fig)
    else:
        plt.savefig('')
        plt.show()
        plt.close()
