import matplotlib.pyplot as plt
import numpy as np
f = lambda x: np.sin(1/x)
x = np.linspace(-2.5, 2.5, 1000)
#pos = np.where(np.abs(np.diff(f(x))) >= 10.0)[0]
x = np.insert(x,0, np.nan)

""" do some stuff here to calculate things """

# color vars
bg = "#f7f7f5"
color = "#252525"
gray = "#777777"

# make a fig
fig = plt.figure(figsize=(11, 8), facecolor=bg)

# plot
plt.plot(f(x), tRecElapsed, '-', color="#dc322f", 
  linewidth=2.0, label='Recursive')
plt.plot(f(x), tAggElapsed, '-', color="#b58900", 
  linewidth=2.0, label='Aggregate')
plt.plot(testNum, tClfElapsed, '-', color="#268bd2", 
  linewidth=2.0, label='Closed Form')

# color settings
ax = plt.gca()
ax.set_axis_bgcolor(bg)
ax.spines['left'].set_color(color)
ax.spines['right'].set_color(color)
ax.spines['bottom'].set_color(color)
ax.spines['top'].set_color(color)
ax.xaxis.label.set_color(color)
ax.tick_params(axis='x', colors=color)
ax.yaxis.label.set_color(color)
ax.tick_params(axis='y', colors=color)

# axis ranges and names
plt.axis([0, nFibs, -1, max(tRecElapsed)+1])
plt.xlabel('nth Fibonacci Number', fontsize=18)
plt.ylabel('Time to Compute, s', fontsize=18)
plt.grid(True, color=gray)

# legend
leg = plt.legend(loc=2)
for text in leg.get_texts():
    text.set_color(color)
frame = leg.get_frame()
frame.set_facecolor(bg)
frame.set_edgecolor(color)

# save it off
fig.savefig('fibonacci.png', 
  facecolor=fig.get_facecolor(),
  edgecolor='none')

