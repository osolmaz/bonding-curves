from math import *
import numpy as np
import matplotlib.pyplot as plt

# Initial bonding curve params
P0 = 0.00001
Delta_p = 1e-11

##### the first number
E_trig0 = 1000

##### 1 - payout_percentage
SIGMA_0 = 0.8
# SIGMA_0 = 0.99

##### # of points
UPPER = 5
# UPPER = 20
# UPPER = 500


def E_trig(alpha):
    return alpha*E_trig0


def sigma(alpha):
    if alpha <= 0:
        return 1.
    else:
        # m = 1/Delta_p*sqrt(2*Delta_p*E_trig0+P0**2)
        # result = 2*Delta_p*alpha*E_trig0/(Delta_p**2*m**2*alpha**2 - P0**2)
        result = 2*Delta_p*E_trig0*alpha/(2*Delta_p*E_trig0*alpha**2+P0**2*(alpha**2-1))
        return result

    # m = 1/Delta_p*sqrt(2*Delta_p*E_trig0/SIGMA_0+P0**2)
    # result = 2*Delta_p*alpha*E_trig0/(Delta_p**2*m**2*alpha**2 - P0**2)

    # if alpha <= 1:
    #     return 1.
    # else:
    #     m = 1/2/Delta_p*sqrt(4*Delta_p*E_trig0/SIGMA_0+P0**2)
    #     result = 2*Delta_p*alpha*E_trig0/(Delta_p**2*m**2*alpha**2 - P0**2)
    #     return result

def sigma_step(alpha):
    return sigma(alpha+1)/sigma(alpha)

# sigma = lambda alpha: SIGMA_0**(alpha-1)

def S_trig(alpha):
    a = P0
    b = Delta_p/2
    c = alpha*E_trig0/sigma(alpha)

    return (sqrt(a**2 + 4*b*c) - a)/(2*b)

def S(R, alpha=None):
    if not alpha:
        current_milestone = floor(R/E_trig0)
    else:
        current_milestone = alpha

    sig = sigma(current_milestone+1)
    P0_ = P0*sig
    Delta_p_ = Delta_p*sig

    R_ = R

    return (sqrt(P0_**2+2*Delta_p_*R_)-P0_)/Delta_p_

def S_no_milestones(R):
    return (sqrt(P0**2+2*Delta_p*R)-P0)/Delta_p

# def S_milestones(R, alpha=0):
#     P_0 =
#     return (sqrt(P0**2+2*Delta_p*R)-P0)/Delta_p


def S_vs_R(start, end, increment):

    R_cur = start
    S = []
    R = []
    P = []
    next_milestone = floor(start/E_trig0) + 1
    just_jumped = False

    while R_cur < end:

        sig = sigma(next_milestone)
        P0_ = P0*sig
        Delta_p_ = Delta_p*sig

        S_cur = (sqrt(P0_**2+2*Delta_p_*R_cur)-P0_)/Delta_p_
        R.append(R_cur)
        S.append(S_cur)

        P.append(P0_ + S_cur*Delta_p_)

        if R_cur + increment > next_milestone*E_trig0 and not just_jumped:
            R_cur = next_milestone*E_trig0
            just_jumped = True
        elif just_jumped:
            R_cur_init = R_cur
            R_cur *= sigma_step(next_milestone)
            next_milestone = floor(R_cur_init/E_trig0) + 1
            just_jumped = False
        else:
            R_cur += increment


    return R, S, P


X = list(range(1,UPPER+1))
Y = [S_trig(x) for x in X]

for alpha in X:
    print(
        'Milestone: %2d ETH: %.1f'%(alpha, E_trig(alpha)),
        'Tokens: {0:,.0f}'.format(S_trig(alpha)))

# Ytmp = [0.] + Y
# Y2 = []

# for y1,y2 in zip(Ytmp, Ytmp[1:]):
    # Y2.append(y2-y1)

plt.xlabel('Milestone (corresponds to multiples of %.0f ETH)'%E_trig(1))
plt.ylabel('Token supply milestone is triggered at')
plt.title('Initial payout: %.2f%% Initial params: P0 = %g Delta_p = %g'%(100.*(1.-sigma_step(1)), P0, Delta_p))

ax = plt.gca()

plt.plot(X, Y, '-o')
# plt.plot(X, Y2)
plt.yticks(Y)
ax.set_yticklabels(["{0:,.0f}".format(y) for y in Y])
plt.xticks(X)
plt.grid()

###################

plt.figure()
R_, S_, P_ = S_vs_R(0, (UPPER)*E_trig0, 1)
plt.plot(R_, S_, label='Supply with milestones', linewidth=3)

X = np.linspace(E_trig0, (UPPER)*E_trig0, 10000)
Y = [S_no_milestones(x) for x in X]
plt.plot(X, Y, label='Supply without milestones')

for i in range(1, UPPER):
    X = np.linspace(0, E_trig0*(i)*sigma_step(i), 10000)
    Y = [S(x, alpha=i) for x in X]
    plt.plot(X, Y, '--', color='gray')


X = list(range(0, UPPER+1))
Y = [S_trig(x) for x in X]
X = [x*E_trig0 for x in X]
plt.plot(X, Y, '--', label='Reference line')
plt.plot(X[1:], Y[1:], 'o', label='Milestones', markersize=8)
plt.grid()

plt.yticks(Y)
ax = plt.gca()
ax.set_yticklabels(["${0:,.0f}$".format(y) for y in Y])

plt.legend()

plt.xlabel('R')
plt.ylabel('S')

##################

X = list(range(1, UPPER+1))
payout_pct = [(1-sigma_step(x)) for x in X]
payout_amount = [(1-sigma_step(x))*E_trig(x) for x in X]

plt.figure()
plt.plot(X, payout_pct, 'o--', markersize=10)
plt.grid()
plt.xticks(X)
plt.xlabel('Milestone')
plt.ylabel('Payout percentage')

plt.figure()
plt.plot(X, payout_amount, 'o--', markersize=10)
plt.grid()
plt.xticks(X)
plt.xlabel('Milestone')
plt.ylabel('Payout amount [ETH]')

##################

plt.figure()
R_, S_, P_ = S_vs_R(0, (UPPER)*E_trig0, 1)
plt.plot(S_, P_, label='Supply with milestones', linewidth=3)


# plt.yticks(Y)
plt.show()


import ipdb; ipdb.set_trace()
