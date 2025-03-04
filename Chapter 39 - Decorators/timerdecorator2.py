import time

def timer(label = '', trace = True):                                            # On decorator args: retain args
    class Timer:
        def __init__(self, func):                                               # On @: retain decorated func
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kargs):                                     # On calls: call original
            start = time.perf_counter()
            result = self.func(*args, **kargs)
            elapsed = time.perf_counter() - start
            self.alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format % values)
            return result
    return Timer
