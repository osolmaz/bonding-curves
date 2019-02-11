from math import *
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)


def return_(P_0, Delta_p, D):
    if D == 0:
        return 1.
    else:
        return (-D*Delta_p - P_0**2 + P_0*sqrt(2*D*Delta_p + P_0**2) - P_0*sqrt(4*D*Delta_p + P_0**2) + sqrt(2*D*Delta_p + P_0**2)*sqrt(4*D*Delta_p + P_0**2))/(D*Delta_p)


P_0 = 1
Delta_ps = [1,1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]

for Delta_p in Delta_ps:
    # X = np.logspace(0., 4., num=10000)
    X = np.linspace(0., 1e4, num=10000)
    Y = [return_(P_0, Delta_p, x) for x in X]

    plt.plot(X, Y, label='$P_0=$%g, $\Delta_p=$%g'%(P_0, Delta_p))
    # plt.semilogx(X, Y)

plt.xlabel('$B$')
plt.ylabel('return')
plt.legend(loc='lower right')
plt.grid()
plt.show()



