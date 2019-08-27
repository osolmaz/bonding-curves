from sympy import *

N = 4

stakes = [Symbol('a_%d'%i) for i in range(N+1)]
reward = [Symbol('b_%d'%i) for i in range(N+1)]
# reward = [1 for i in range(N+1)]


result1 = 0

for i in range(N+1):
    result1 += stakes[i]*reward[i]

pprint(result1)

def S(n):
    result = 0
    for i in range(n+1):
        result += reward[i]
    return result


result2 = stakes[N]*S(N)
# result2 = 0

for i in range(1, N+1):

    # import ipdb; ipdb.set_trace()
    result2 -= (stakes[i] -stakes[i-1])*S(i-1)

pprint(simplify(result2))
