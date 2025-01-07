def gen():
    for i in range(10):
        X = yield i
        print(X)

G = gen()
next(G)         # Must call next() first, to start generator

G.send(77)      # Advance, and send value to yield expression

G.send(88)      # next() and X.__next__() send None

next(G)
