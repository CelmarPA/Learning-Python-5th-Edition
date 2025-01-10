"""Test tje relative speed of iteration tool alternatives."""

import sys, timer       # Import timer functions

reps = 10000

repslist = list(range(reps))        # Hoist out, list in both 2.X/3.X

def forLoop():
    res = []
    for x in repslist:
        res.append(F(x))
    return res

def F(x): return x

def lisComp():
    return [F(x) for x in repslist]

def mapCall():
    return list(map(F, repslist))          # list() in 3.X only

def genExpr():
    return list(F(x) for x in repslist)       # list() in 2.X + 3.X

def genFunc():
    def gen():
        for x in repslist:
            yield F(x)
    return list(gen())      # list in 2.X + 3.X

print(sys.version)

for test in (forLoop, lisComp, mapCall, genExpr, genFunc):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print('%-9s: %.5f => [%s...%s]' % (test.__name__, bestof, result[0], result[-1]))
