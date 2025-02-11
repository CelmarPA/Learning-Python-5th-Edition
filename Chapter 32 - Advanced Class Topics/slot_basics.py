class Limiter(object):
    __slots__ = ['age', 'name', 'job']

x = Limiter()

# Must assign before use
# print(x.age)   # AttributeError: 'Limiter' object has no attribute 'age'

x.age = 40                      # Looks like instance data

print(x.age)

# x.ape = 1000      # Illegal: not in __slots__   # AttributeError: 'limiter' object has no attribute 'ape'
