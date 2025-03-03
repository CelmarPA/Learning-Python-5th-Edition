# A call tracer decorator for both functions and methods

def tracer(func):                                               # Use function, not class with __call__
    calls = 0                                                   # Else "self" is decorator instance only!
    def onCall(*args, **kwargs):                                # Or in 2.X+3.X: use [onCall.calls += 1]
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall

if __name__ == "__main__":

    # Applies to simple functions

    @tracer
    def spam(a, b, c):                          # spam = tracer(spam)
        print(a + b + c)                        # onCall remembers spam

    @tracer
    def eggs(N):
        return 2 ** N

    spam(1, 2, 3)                      # Runs onCall(1, 2, 3)
    spam(a = 4, b = 5, c = 6)
    print(eggs(32))

    # Applies to class-level method function too!
    class Person:
        def __init__(self, name, pay):
            self.name = name
            self.pay = pay

        @tracer
        def giveRaise(self, percent):           # giveRaise = tracer(giveRaise)
            self.pay *= (1.0 + percent)         # onCall remembers giveRaise

        @tracer
        def lastName(self):                     # lastName = tracer(lastName
            return self.name.split()[-1]

print('methods...')

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jone',  100000)

print((bob.name, sue.name))

sue.giveRaise(.10)                              # Runs onCall(sue, .10)

print(int(sue.pay))

print(bob.lastName(), sue.lastName())           # Runs onCall(bob), lastName in scopes

print('-' * 80)

# Using descriptors to decorate methods

class Tracer(object):                                                   # A decorator+descriptor
    def __init__(self, func):                                           # On @ decorator
        self.calls = 0                                                  # Save func for later call
        self.func = func

    def __call__(self, *args, **kwargs):                                # On call to original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):                                 # On method attribute fetch
        return Wrapper(self, instance)

class Wrapper:
    def __init__(self, desc, subj):
        self.desc = desc
        self.subj = subj

@Tracer
def spam(a, b, c):
    print(a + b + c)

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @Tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @Tracer
    def lastName(self):
        return self.name.split()[-1]
