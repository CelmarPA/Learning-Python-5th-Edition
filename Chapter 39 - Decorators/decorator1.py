class Tracer:
    def __init__(self, func):                                       # On @ decoration: save original func
        self.calls = 0
        self.func = func

    def __call__(self, *args):                                     # On later calls: run original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))

@Tracer
def spam(a, b, c):                  # spam = tracer(spam)
    print(a + b + c)                # Wraps spam in a decorator object

spam(1 , 2, 3)                # Really calls the tracer wrapper object

spam('a', 'b', 'c')           # Invokes __call__ in class

print(spam.calls)                   # Number calls in wrapper state information

print(spam)

print('-' * 80)

calls = 0

def tracer(func, *args):
    global calls
    calls += 1
    print('call %s to %s' % (calls, func.__name__))

def spam(a, b, c):
    print(a, b, c,)

spam(1, 2, 3)             # Normal nontraced call: accidental?

tracer(spam, 1, 2, 3)        # Special-traced call without decorators
