import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure(figsize=(5, 4))
# Generate some data
mu, sigma = 1e7, 1e6
s = np.random.normal(mu, sigma, 10000)
# Plot it
plt.hist(s, 30, histtype='step')
# Format it
ax = plt.gca()
ax.minorticks_on()
ax.set_xlabel('Vertex position [mm]', x=1, ha='right')
ax.set_ylabel('Candidates', y=1, ha='right')
fig.set_tight_layout(True)
# Plot the figure once, then append the offset text to the x-axis label
# Hide the offset text as we no longer need it, then redraw the figure
fig.savefig('vertex-position.svg')
offset = ax.get_xaxis().get_offset_text()
ax.set_xlabel('{0} {1}'.format(ax.get_xlabel(), offset.get_text()))
offset.set_visible(False)
fig.savefig('vertex-position.svg')