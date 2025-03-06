# Quiz Chapter 39

# 1. Method decorators:
"""
File timedeco.py (3.X + 2.X)
Call timer decorator for both functions and methods.
"""

import time
from math import lgamma


def timer(label = '', trace = True):
    def onDecorator(func):
        def onCall(*args, **kargs):
            start = time.perf_counter()
            result = func(*args, **kargs)
            elapsed = time.perf_counter() - start
            onCall.alltime += elapsed
            if trace:
                format = '%s%s: %.5f, %.5f'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format % values)
            return result
        onCall.alltime = 0
        return onCall
    return onDecorator

"""
File timerdeco_test.py
"""

# from __future__ import print_function
# from timerdeco import timer
import sys

force = list if sys.version_info[0] == 3 else (lambda X: X)

print('---------------------------------------------------')

# Test on functions

@timer(trace = True, label = '[CCC]==>')
def listcomp(N):                                                # Like listcomp = timer(...)(listcomp)
    return [x * 2 for x in range(N)]                            # listcomp(...) triggers onCall

@ timer('[MMM]==>')
def mapcall(N):
    return force(map((lambda  x: x * 2), range(N)))             # list() for 3.X views

for func in (listcomp, mapcall):
    result = func(5)                                            # Time for this call, all calls, return value
    func(5000000)
    print(result)
    print('alltime = %s\n' % func.alltime)                      # Total time for all calls

print('---------------------------------------------------')

# Test on methods

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @timer()
    def giveRaise(self, percent):                               # giveRaise = timer()(giveRaise)
        self.pay *= (1.0 + percent)                             # tracer remembers giveRaise

    @timer(label = '**')
    def lastName(self):                                         # lastName = timer(...)(lastName)
        return self.name.split()[-1]                            # alltime per class, not instance

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)

bob.giveRaise(.10)
sue.giveRaise(.20)                                              # runs onCall(sue, .10)

print(int(bob.pay),  int(sue.pay))
print(bob.lastName(), sue.lastName())
print('%.5f %.5f' % (Person.giveRaise.alltime, Person.lastName.alltime))

print('---------------------------------------------------')

# 2. Class decorators:

"""
File access.py (3.X + 2.X)
Class decorator with Private and Public attribute declarations.
Controls external access to attributes stored on an instance, or
inherited by it from its classes in any fashion.

Private declares attribute names that cannot be fetched or assigned
outside the decorated class, and Public declares all the names that can.

Caveats: in 3.X catches built-ins coded in BuiltinMixins only (expand me);
as coded, Public may be less useful than Private for operator overloading.
"""

from access_builtins import BuiltinsMixin       # A partial set

traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
    def onDecorator(aClass):
        if not __debug__:
            return aClass
        else:
            class onInstance(BuiltinsMixin):
                def __init__(self, *args, **kargs):
                    self.__wrapped = aClass(*args, **kargs)

                def __getattr__(self, attr):
                    trace('get:', attr)
                    if failIf(attr):
                        raise TypeError('private attribute fetch: ' + attr)
                    else:
                        return getattr(self.__wrapped, attr)

                def __setattr__(self, attr, value):
                    trace('set:', attr, value)
                    if attr == '_onInstance__wrapped':
                        self.__dict__[attr] = value
                    elif failIf(attr):
                        raise TypeError('private attribute change: ' + attr)
                    else:
                        setattr(self.__wrapped, attr, value)
            return onInstance
    return onDecorator

def Private(*attributes):
    return accessControl(failIf = (lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf = (lambda attr: attr not in attributes))

"""
File access_builtins.py (from access2_builtins2b.py)
Route some built-in operations back to proxy class __getattr__, so they
work the same in 3.X as direct by-name calls and 2.X's default classic classes.
Expand me as needed to include other __X__ names used by proxied objects.
"""

class BuiltinsMixin:
    def reroute(self, attr, *args, **kargs):
        return self.__class__.__getattr__(self, attr)(*args, **kargs)

    def __add__(self, other):
        return self.reroute('__add__', other)

    def __str__(self):
        return self.reroute('__str__')

    def __getitem__(self, index):
        return self.reroute('__getitem__', index)

    def __call__(self, *args, **kargs):
        return self.reroute('__call__', *args, **kargs)
    # Plus any others used by wrapped objects in 3.X only

"""
File: access-test.py
Test code: separate file to allow decorator reuse.
"""

import sys
# from access import Private, Public

print('---------------------------------------------------------')

# Test 1: names are public if not private

@Private('age')                                     # Person = Private('age')(Person)
class Person:                                       # Person = onInstance with state
    def __init__(self, name, age):
        self.name = name
        self.age = age                              # Inside accesses run normally

    def __add__(self, N):
        self.age += N                               # Built-ins caught by mix-in in 3.X

    def __str__(self):
        return '%s: %s' % (self.name, self.age)

X = Person('Bob', 40)

print(X.name)                                       # Outside accesses validated

X.name = 'Sue'

print(X.name)

X + 10

print(X)

try:
    t = X.age                                       # FAILS unless "python -O"
except:
    print(sys.exc_info()[1])

try:
    X.age = 999                                     # ditto
except:
    print(sys.exc_info()[1])

print('---------------------------------------------------------')

# Test 2: names are private if not public
# Operators must be non-Private or Public in BuiltinMixin used

@Public('name', '__add__', '__str__', '__coerce__')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, N):
        self.age += N                               # Built-ins caught by mix-in in 3.X

    def __str__(self):
        return '%s: %s' % (self.name, self.age)

X = Person('Bob', 40)                     # X is an onInstance

print(X.name)                                        # onInstance embeds Person

X.name = 'Sue'

print(X.name)

X + 10

print(X)

try:
    t = X.age                                        # FAILS unless "python -O"
except:
    print(sys.exc_info()[1])

try:
    X.age = 999                                      # ditto
except:
    print(sys.exc_info()[1])

print('---------------------------------------------------------')

# 3. Generalized argument validations:

"""
File argtest.py: (3.X + 2.X) function decorator that performs
arbitrary passed-in validations for arguments passed to any
function method. Range and type tests are two example uses;
valuetest handles more arbitrary tests on an argument's value.

Arguments are specified by keyword to the decorator. In the actual
call, arguments may be passed by position or keyword, and defaults
may be omitted. See self-test code below for example use cases.

Caveats: doesn't fully support nesting because call proxy args
differ; doesn't validate extra args passed to a decoratee's *args;
and may be no easier than an assert except for canned use cases.
"""

trace = False

def rangetest(**argchecks):
    return argtest(argchecks, lambda arg, vals: arg < vals[0] or arg > vals[1])

def typetest(**argchecks):
    return argtest(argchecks, lambda arg, type: not isinstance(arg, type))

def valuetest(**argchecks):
    return argtest(argchecks, lambda arg, tester: not tester(arg))

def argtest(argchecks, failIf):                                                 # Validate args per failIf + criteria
    def onDecorator(func):                                                      # onCall retains func, argchecks, failIf
        if not __debug__:                                                       # No-op if "python -O main.py args..."
            return func
        else:
            code = func.__code__
            expected = list(code.co_varnames[:code.co_argcount])
            def onError(argname, criteria):
                errfmt = '%s argument "%s" not %s'
                raise TypeError(errfmt % (func.__name__, argname, criteria))

            def onCall(*pargs, **kargs):
                positionals = expected[:len(pargs)]
                for (argname, criteria) in argchecks.items():                   # For all to test
                    if argname in kargs:                                        # Passed by name
                        if failIf(kargs[argname], criteria):
                            onError(argname, criteria)

                    elif argname in positionals:                                # Passed by posit
                        position = positionals.index(argname)
                        if failIf(pargs[position], criteria):
                            onError(argname, criteria)

                    else:                                                       # Not passed-dflt
                        if trace:
                            print('Argument "%s" defaulted' % argname)
                return func(*pargs, **kargs)
            return onCall
    return onDecorator

if __name__ == '__main__':
    import sys
    def fails(test):
        try:
            result = test()
        except:
            print('[%s]' % sys.exc_info()[1])
        else:
            print('?%s?' % result)
    print('--------------------------------------------------------------------')

    # Canned use cases: ranges, types

    @rangetest(m = (1, 12), d = (1, 31), y = (1900, 2025))
    def date(m, d, y):
        print('date = %s/%s/%s' % (m, d, y))

    date(1, 2, 1960)
    fails(lambda: date(1, 2, 3))

    @typetest(a = int, c = float)
    def sum(a, b, c, d):
        print(a + b + c + d)

    sum(1, 2, 3.0, 4)
    sum(1, d = 4, b = 2, c = 3.0)

    fails(lambda: sum('spam', 2, 99, 4))
    fails(lambda: sum(1, d = 4, b = 2, c = 99))

    print('--------------------------------------------------------------------')

    # Arbitrary / mixed tests

    @valuetest(word1 = str.islower, word2 = (lambda x: x[0].isupper()))
    def msg(word1 = 'mighty', word2 = 'Larch', label = 'The'):
        print('%s %s %s' % (label, word1, word2))

    msg()                                                       # word1 and word2 defaulted
    msg('majestic', 'Moose')

    fails(lambda: msg('Giant', 'Redwood'))
    fails(lambda: msg('great', word2 = 'elm'))

    print('--------------------------------------------------------------------')

    # Manual type and range tests

    @valuetest(A = lambda x: isinstance(x, int), B = lambda x: x > 0 and x < 10)
    def manual(A, B):
        print(A + B)

    manual(100 ,2)

    fails(lambda: manual(1.99, 2))
    fails(lambda: manual(100, 20))

    print('--------------------------------------------------------------------')
    # Nesting: runs both, by nesting proxies on original.
    # Open issue: outer levels do not validate positionals due
    # to call proxy function's differing argument signature;
    # when trace=True, in all but the last of these "X" is
    # classified as defaulted due to the proxy's signature.

    @rangetest(X = (1, 10))
    @typetest(Z = str)
    def nester(X, Y, Z):
        return ('%s-%s-%s' % (X, Y, Z))

    print(nester(1, 2, 'spam'))             # Original function runs properly
    fails(lambda: nester(1, 2, 3))          # Nested typetest is run: positional
    fails(lambda: nester(1, 2, Z = 3))         # Nested typetest is run: keyword
    fails(lambda: nester(0, 2, 'spam'))     # <==Outer rangetest not run: posit.
    fails(lambda: nester(X = 0, Y = 2, Z = 'spam'))  # Outer rangetest is run: keyword

print('--------------------------------------------------------------------')

# File argtest_testmeth.py

# from argtest import rangetest, typetest

class C:
    @rangetest(a = (1, 10))
    def meth1(self, a):
        return a * 1000

    @typetest(a = int)
    def meth2(self, a):
        return a * 1000

X = C()

print(X.meth1(5))

# X.meth1(20)

print(X.meth2(20))

# X.meth2(20.9)
