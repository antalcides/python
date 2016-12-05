#!/usr/bin/env python
import numpy as np
import scipy
import pylab as plt

t=np.linspace(-6,+6,2**8)
dt=t[1]-t[0]
h=np.cos(2*np.pi*t)
h[(t>4.) | (t<-4)]=0.

H=np.fft.fft(h)
print H[:3]
f=np.fft.fftfreq(len(t),d=dt)

plt.subplot(121)
#plt.subplots_adjust(wspace=0.3)
plt.plot(t,h,'k-')
plt.xlabel('t')
plt.ylabel('h(t)')
plt.subplot(122)
plt.plot(f,H.real,'r-',f,H.imag,'b-')
plt.xlabel('f')
plt.ylabel('H(f)')
plt.tight_layout()
plt.show()
