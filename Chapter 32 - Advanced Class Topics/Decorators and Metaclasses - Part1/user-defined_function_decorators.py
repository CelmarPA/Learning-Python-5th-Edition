class Tracer:
    def __init__(self, func):                                           # Remember original, init counter
        self.call = 0
        self.func = func

    def __call__(self, *args):                                          # On later calls: add logic, run original
        self.call += 1
        print('call %s to %s' % (self.call, self.func.__name__))
        return self.func(*args)

@Tracer                                                                 # Same as spam = tracer(spam)
def spam(a, b, c):                                                      # Wrap spam in a decorator object
    return a + b + c

print(spam(1, 2, 3))                                              # Really calls the tracer wrapper object
print(spam('a', 'b', 'c'))                                        # Invokes __call__ in class

def tracer(func):                                                       # Remember original
    def oncall(*args):                                                  # On later calls
        oncall.calls += 1
        print('call %s to %s' % (oncall.calls, func.__name__))
        return func(*args)

    oncall.calls = 0
    return oncall

class C:
    @tracer
    def spam(self, a, b, c): return a + b + c                           # Same output as tracer1 (in tracer2.py)

x = C()

print(x.spam(1, 2, 3))

print(x.spam('a', 'b', 'c'))
