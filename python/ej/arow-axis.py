import matplotlib.pyplot as plt
import numpy as np
ax = plt.subplot(1,1,1)
  
al = 7 # arrow length in points
arrowprops=dict(clip_on=False, # plotting outside axes on purpose
     frac=1., # make end arrowhead the whole size of arrow
     headwidth=al, # in points
     facecolor='k')
kwargs = dict(  
                  xycoords='axes fraction',
                  textcoords='offset points',
                  arrowprops= arrowprops,
               )
  
ax.annotate("",(1,0),xytext=(-al,0), **kwargs) # bottom spine arrow
ax.annotate("",(0,1),xytext=(0,-al), **kwargs) # left spin arrow
  
  # hide the top and right spines
#[sp.set_visible(False) for sp in ax.spines['top'],ax.spines['right']]
  
  #hide the right and top tick marks
ax.yaxis.tick_left()
ax.xaxis.tick_bottom()
  
x = np.linspace(-5,5,50)
ax.plot(x, np.sin(x))
  
  # adjust the view a little bit
ax.set_xlim(-5,5)
ax.set_ylim(-1.1,1.1)
plt.show()
