from sympy import *

# price_increment = 1e-8
# initial_price = 1e-7

initial_price = Symbol('P_0')
price_increment = Symbol('Delta_p')
supply = Symbol('S')
eth = Symbol('R')


price_supply = initial_price + price_increment*supply
# price_supply = sqrt(supply)

total_eth = integrate(price_supply, (supply, 0, supply))

pprint(total_eth)

supply_eth = solve(eth - total_eth, supply)[0]

pprint(supply_eth)
# supply_fun = lambdify(eth, supply_eth)

# supply_eth = (sqrt(initial_price**2+2*price_increment*eth) - initial_price)/price_increment

price_eth = price_supply.subs(supply, supply_eth)


pprint(price_eth)
print()

pprint(diff(price_eth, eth))

print()

initial_deriv = simplify(diff(price_eth, eth).subs(eth, 0))
pprint(initial_deriv)


interval = Symbol('D')

bound1 = supply_eth.subs(eth, interval)
bound2 = supply_eth.subs(eth, 2*interval)

eth1 = integrate(price_supply, (supply, 0, bound1))
eth2 = integrate(price_supply, (supply, bound2-bound1, bound2))

return_ = simplify(eth2/eth1)

pprint(return_)
print(return_)
pprint(limit(return_, interval, 'oo'))
# pprint(limit(return_, interval, 'oo').evalf())

print()
pprint(limit(return_, interval, '0'))
print()


# import ipdb; ipdb.set_trace()


# pprint(simplify(return_.subs(interval, 1)))

# price_increment = 1e-8
# initial_price = 1e-7


return_ = return_.subs([
    # (interval, 100),
    (initial_price, 1e-7),
    (price_increment, 1e-8),
    # (initial_price, 0.0001),
    # (price_increment, 1e-12),
])

return_fun = lambdify(interval, return_)

# import ipdb; ipdb.set_trace()
pprint(return_fun(1))

# import matplotlib.pyplot as plt
# import numpy as np

# X = np.linspace(0, 100000000, 10000)
# plt.plot(X, [return_fun(x) for x in X])
# plt.show()

# import ipdb; ipdb.set_trace()

