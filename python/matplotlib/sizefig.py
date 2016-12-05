#matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2

fig = plt.figure(figsize=(5, 5))
plt.scatter(x, y, s=area, alpha=0.5)
plt.show()
tikz_save( 'figsize.tikz' )
plt.savefig('figsize.pdf')
