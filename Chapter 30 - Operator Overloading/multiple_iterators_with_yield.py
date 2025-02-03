from squares_yield import Squares

S = Squares(1, 5)

I = iter(S)

print(next(I), next(I))

J = iter(S)

print(next(J))

print(next(I))

S = Squares(1, 3)

for i in S:
    for j in S:
        print('%s:%s' % (i, j), end = ' ')

