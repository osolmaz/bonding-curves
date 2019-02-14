from math import *
import numpy as np
import matplotlib.pyplot as plt

# Initial bonding curve params
P0 = 1.

params = [
    (P0, 0),
    # (P0, 0.00001),
    (P0, 0.0001),
    (P0, 0.001),
    (P0, 0.01),
    (P0, 0.1),
    (P0, 1),
]



def S(P0, Delta_p, R):
    if Delta_p == 0:
        return R/P0
    else:
        return (sqrt(P0**2+2*Delta_p*R)-P0)/Delta_p

for param in params:
    X = np.linspace(0,1000, 10000)
    Y = [S(param[0], param[1], x) for x in X]

    plt.plot(X, Y, label='P0=%g, Delta_p=%g'%(param[0], param[1]))

plt.xlabel('R')
plt.ylabel('S')
plt.legend()
plt.grid()

plt.show()


import ipdb; ipdb.set_trace()
