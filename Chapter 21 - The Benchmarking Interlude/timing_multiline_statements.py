import timeit

print(min(timeit.repeat(number = 10000, repeat = 3,
                        stmt = "L = [1, 2, 3, 4, 5]\nfor i in range(len(L)): L[i] += 1")))

print(min(timeit.repeat(number = 10000, repeat = 3,
                        stmt = "L = [1, 2, 3, 4, 5]\ni = 0\nwhile i < len(L):\n\tL[i] += 1\n\ti += 1")))

print(min(timeit.repeat(number = 10000, repeat = 3,
                        stmt = "L = [1, 2, 3, 4, 5]\nM = [x + 1 for x in L]")))
