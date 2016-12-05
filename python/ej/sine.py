import numpy as np
import matplotlib.pyplot as plt


#http://matplotlib.sourceforge.net/examples/pylab_examples/spine_placement_demo.html


fig = plt.figure(figsize=(4, 5))

ax = fig.add_subplot(111)



x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = np.sin(x)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')


ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.plot(x, y,linewidth="3", alpha=0.3)

ax.plot([0, np.pi/2], [1, 1], ls="--", color="green", linewidth="3",alpha=0.5)
ax.plot([np.pi/2, np.pi/2], [1, 0], ls="--", color="red", linewidth="3",alpha=0.5)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')


ax.set_xlim(-2*np.pi, 2*np.pi)

xticker = np.arange(-np.pi-np.pi/2, np.pi+np.pi, np.pi/2)
xlabels = [r"$\frac{-3\pi}{2}$", r"${-\pi}$",r"$\frac{-\pi}{2}$","",r"$\frac{pi}{2}$",r"${\pi}$",r"$\frac{3\pi}{2}$"]

ax.set_xticks(xticker)
ax.set_xticklabels(xlabels, size=17)

ax.text(np.pi, 1.1, "y=sin(x)")

ax.set_ylim(-1.5, 1.5)
yticker = np.arange(-1, 2, 1)
ax.set_yticks(yticker)
#remove zero




plt.show()
