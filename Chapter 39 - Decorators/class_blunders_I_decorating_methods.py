from idlelib.configdialog import tracers


class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

@Tracer
def spam(a, b, c):                  # spam = tracer(spam)
    print(a + b + c)                # spam = tracer(spam)

@Tracer
def eggs(x, y):
    print(x ** y)

spam(1 , 2, 3)                # spam = tracer(spam)
spam(a = 4, b = 5, c = 6)           # spam saved in an instance attribute

eggs(2, 16)
eggs(4, y = 4)

print('-' * 80)

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @Tracer
    def giveRaise(self, percent):           # giveRaise = tracer(giveRaise)
        self.pay *= (1.0 + percent)

    @Tracer
    def lastName(self):                     # lastName = tracer(lastName)
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)        # tracer remembers method funcs
bob.giveRaise(.25)                                 # Runs tracer.__call__(???, .25)

# TypeError: giveRaise() missing 1 required positional argument: 'percent'

print(bob.lastName())

# TypeError: lastName() missing 1 required positional argument: 'self'
