import sys, timer2

reps = 10000
repslist = range(reps)

from math import sqrt

def mathMod():
    for i in repslist:
        res = sqrt(i)
    return res

def powCall():
    for i in repslist:
        res = pow(i, .5)
    return res

def powExpr():
    for i in repslist:
        res = i ** .5
    return res

print(sys.version)

for test in (mathMod, powCall, powExpr):
    elapsed, result = timer2.bestoftotal(test, _reps1 = 3, _reps = 1000)
    print('%s %.5f => %s' % (test.__name__, elapsed, result))

    