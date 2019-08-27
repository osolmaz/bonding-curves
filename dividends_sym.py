from sympy import *

N = 4

stakes = [Symbol('stake_%d'%i) for i in range(N+1)]
reward = [Symbol('reward_%d'%i) for i in range(N+1)]
T = [Symbol('T_%d'%i) for i in range(N+1)]

t1 = 0
t2 = N

result1 = 0

for i in range(t1, t2+1):
    result1 += stakes[i]*reward[i]/T[i]

pprint(result1)

def S(n):
    result = 0
    for i in range(n+1):
        result += reward[i]/T[i]
    return result


result2 = stakes[t2]*S(t2)
# result2 = 0

for i in range(t1+1, t2+1):
    result2 -= (stakes[i] -stakes[i-1])*S(i-1)

pprint(simplify(result2))
