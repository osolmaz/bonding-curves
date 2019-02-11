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

# loc = plticker.MultipleLocator(base=1.0) # this locator puts ticks at regular intervals
# ax = plt.gca()
# ax.yaxis.set_major_locator(loc)

P_0 = 1e-7
Delta_ps = [1e-8]

for Delta_p in Delta_ps:
    # X = np.logspace(0., 4., num=10000)
    X = np.linspace(0., 80000, num=10000)
    Y = [return_(P_0, Delta_p, x) for x in X]

    plt.plot(X, Y, label='$P_0=$%g, $\Delta_p=$%g'%(P_0, Delta_p))
    # plt.semilogx(X, Y)

    print(return_(P_0, Delta_p, 1)/P_0)
    print(return_(P_0, Delta_p, 10)/P_0)
    print(return_(P_0, Delta_p, 100)/P_0)
    print(return_(P_0, Delta_p, 1000)/P_0)
    print(return_(P_0, Delta_p, 10000)/P_0)
    print(return_(P_0, Delta_p, 100000)/P_0)

print(return_(P_0, Delta_p, 80000)/return_(P_0, Delta_p, 100))

plt.xlabel('$R$')
plt.ylabel('$P$')
plt.legend(loc='lower right')
plt.grid()
plt.show()



