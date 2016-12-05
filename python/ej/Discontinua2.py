from pylab import *
import matplotlib 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save
plt.rc('text', usetex=True)
matplotlib.colors.ColorConverter.colors['mc1'] = (0.,0.69,0.92)
x = linspace(-2, 2.0, 1000) 
y = np.sin(1/x)  
figure()
plt.plot(x, y,label=r"$f(x)=\sin(\frac{1}{x})$",color='mc1', linestyle='-', lw=1.5)
xlabel('X') 
ylabel('Y') 
#title('A Simple Plot') 
grid()
xlim(-2,2)
ylim(-1.5,1.5)
plt.legend(loc=1)
show()
tikz_save( 'discontinua2a.tikz' );
plt.savefig('discontinua2a.pdf')
