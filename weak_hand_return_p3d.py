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


P_0 = 1e-7
Delta_ps = [1e-8]

for Delta_p in Delta_ps:
    # X = np.logspace(0.001, 0.01, num=100000)
    X = np.linspace(0., 1, num=10000)
    Y = [return_(P_0, Delta_p, x) for x in X]

    plt.plot(X, Y, label='$P_0=$%g, $\Delta_p=$%g'%(P_0, Delta_p))
    # plt.semilogx(X, Y)
    print(return_(P_0, Delta_p, 1.))
    print(return_(P_0, Delta_p, 100.))

# plt.ylim(1, 1.83)

plt.xlabel('$B$')
plt.ylabel('return')
plt.legend(loc='lower right')
plt.grid()
plt.show()



