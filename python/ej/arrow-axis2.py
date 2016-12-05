import matplotlib.pyplot as plt

fig, ax = plt.subplots()

#-- Set axis spines at 0
for spine in ['left', 'bottom']:
    ax.spines[spine].set_position('zero')

# Hide the other spines...
for spine in ['right', 'top']:
    ax.spines[spine].set_color('none')

#-- Decorate the spins
arrow_length = 20 # In points

# X-axis arrow
#ax.annotate('X', xy=(1, 0), xycoords=('axes fraction', 'data'), 
            #xytext=(-4, 0), textcoords='offset points',
            #ha='left', va='center',
            #arrowprops=dict(arrowstyle='-|>', fc='black'))
ax.annotate("",
            xy=(-2, 0), xycoords='data',
            xytext=(0, 0), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )           ################################################
            
            ################################3

# Y-axis arrow
ax.annotate('Y', xy=(0, 1), xycoords=('data', 'axes fraction'), 
            xytext=(0, arrow_length), textcoords='offset points',
            ha='center', va='bottom',
            arrowprops=dict(arrowstyle='<|-', fc='black'))

#-- Plot
ax.axis([-4, 10, -4, 10])
ax.grid()

plt.show()

