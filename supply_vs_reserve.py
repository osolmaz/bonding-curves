from math import *
import numpy as np
import matplotlib.pyplot as plt

# Initial bonding curve params
# P0 = 0.00001
# Delta_p = 1e-11
# Delta_p = 1e-20

params = [
    (1e-5, 1e-11),
    (1e-5, 1e-12),
    (1e-5, 1e-13),
]


def S(P0, Delta_p, R):
    return (sqrt(P0**2+2*Delta_p*R)-P0)/Delta_p

for param in params:
    X = np.linspace(0,10000, 10000)
    Y = [S(param[0], param[1], x) for x in X]

    plt.plot(X, Y, label='P0=%g, Delta_p=%g'%(param[0], param[1]))

plt.legend()
plt.grid()

plt.show()


import ipdb; ipdb.set_trace()
