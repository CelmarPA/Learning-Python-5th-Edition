# Caveat: range still differs - a list in 2.X, an iterable in 3.X
# Caveat: timer won't work on methods as coded (see a quiz solution)

import time, sys

force = list if sys.version_info[0] == 3 else (lambda X: X)

class Timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0

    def __call__(self, *args, **kargs):
        start = time.perf_counter()
        result = self.func(*args, **kargs)
        elapsed = time.perf_counter() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result

@Timer
def listcomp(N):
    return [x * 2 for x in range(N)]

@Timer
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))

result = listcomp(5)                        # Time for this call, all calls, return value

listcomp(50000)
listcomp(500000)
listcomp(1000000)

print(result)
print('alltime = %s' % listcomp.alltime)    # Total time for all listcomp calls

print('')

result = mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)

print(result)
print('alltime = %s' % mapcall.alltime)    # Total time for all mapcall calls

print('\n**map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))
