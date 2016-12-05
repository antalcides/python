#!/usr/bin/env python
import numpy as np
import scipy
import scipy.ndimage
import pylab as plt

x=np.arange(-1,1.,0.01)
y=np.ones_like(x)
y[(x<-0.5) | (x>+0.5)]=0.

c=scipy.ndimage.convolve1d(y, y)
c2=scipy.ndimage.convolve1d(y, c)

print c.shape

plt.subplot(131)
plt.plot(y,'r-')
plt.subplot(132)
plt.plot(c,'b-')
plt.subplot(133)
plt.plot(c2,'g-')
plt.tight_layout()
plt.show()
