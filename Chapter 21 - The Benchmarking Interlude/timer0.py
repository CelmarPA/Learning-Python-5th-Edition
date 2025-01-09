import time

def timer(func, *args):         # Simplistic timing function
    # start = time.clock()        # time.clock() was removed in Python 3.8
    start = time.perf_counter()     # Now use time.perf_counter()
    for i in range(1000):
        func(*args)
    return time.perf_counter() - start         # Total elapsed time in seconds




# Measure CPU time

def cpuTimer(func, *args):
    start = time.process_time()
    for i in range(1000000):
        func(*args)
    return time.process_time() - start

