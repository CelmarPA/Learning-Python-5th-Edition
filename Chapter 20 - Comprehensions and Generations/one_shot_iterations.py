def myzip(*args):
    iters = list(map(iter, args))
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)

# print(list(myzip('abc', 'lmnop')))

# From Python 3.7 a generator that raises a "StopIteration" exception,
# is automatically converted to a RuntimeError.

def myzip2(*args):
    iters = list(map(iter, args))
    while True:
        try:
            res = [next(i) for i in iters]
            yield tuple(res)
        except StopIteration:
            return

print(list(myzip('abc', 'lmnop')))

print(list(myzip([1, 2, 3], [4, 5])))

print(list(myzip('ab', [1, 2], (10, 20, 30))))
