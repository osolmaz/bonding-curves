import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

price_increment = 1e-12
initial_price = 0.0001

# price_increment = 1e-8
# initial_price = 1e-7


price_supply = lambda supply: initial_price + price_increment*supply

supply_eth = lambda eth: (sqrt(initial_price**2+2*price_increment*eth) - initial_price)/price_increment

# price_eth = lambda eth: price_supply(supply_eth(eth))

price_eth = lambda eth: sqrt(2*eth*price_increment+initial_price**2)


current_supply = 2312114.
current_eth = 26729.

print(supply_eth(current_eth))
print(price_eth(current_eth))

X = np.linspace(0, 30000, 100000)
Y = [price_eth(x) for x in X]

print('Ratio:', (price_eth(0.000000001)-price_eth(0))/0.000000001)
print('Test:', price_increment/initial_price)

plt.xlabel('Deposited ETH')
plt.ylabel('Token Price [ETH]')
plt.title('Deposited ETH vs Token Price for suggested params:\ninitial_price = %g ETH and price_increment = %g ETH'%(initial_price, price_increment))
plt.ylim([0, max(Y)*1.1])
plt.xlim([min(X), max(X)])
plt.plot(X, Y)
plt.grid()
plt.show()
