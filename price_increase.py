from math import *
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)


def return_(P_0, Delta_p, D):
    return sqrt(P_0**2 + 2*Delta_p*D)

import matplotlib.ticker as plticker

loc = plticker.MultipleLocator(base=1.0) # this locator puts ticks at regular intervals
ax = plt.gca()
ax.yaxis.set_major_locator(loc)

P_0 = 1
Delta_ps = [0.005, 0.002, 0.001, 0.0005, 0.0002]

for Delta_p in Delta_ps:
    # X = np.logspace(0., 4., num=10000)
    X = np.linspace(0., 1e4, num=10000)
    Y = [return_(P_0, Delta_p, x) for x in X]

    plt.plot(X, Y, label='$P_0=$%g, $\Delta_p=$%g'%(P_0, Delta_p))
    # plt.semilogx(X, Y)

plt.xlabel('$R$')
plt.ylabel('$P$')
plt.legend(loc='lower right')
plt.grid()
plt.show()


