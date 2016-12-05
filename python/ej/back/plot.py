import matplotlib.pyplot as plt
#import plot, show
import pylab as pl
from numpy import arange
x = pl.arange(-4, 5, 0.01)
pl.axes( )
plt.axhline(0, linestyle='--', linewidth=2, color='gray')
plt.axvline(0, linestyle='--', linewidth=2, color='gray')
pl.grid(True)
pl.axis([-4, 5, -3, 6])
plt.plot(x, x ** 2 / (x ** 2 - 3))
plt.show()
pl.savefig("grafica.pdf")

