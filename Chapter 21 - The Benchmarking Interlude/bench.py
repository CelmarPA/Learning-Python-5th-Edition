from timer2 import total, bestof, bestoftotal

print(total(pow, 2, 1000)[0])       # 2 ** 1000, 1K dflt reps

print(total(pow, 2, 1000, _reps = 1000)[0])         # 2 ** 1000, 1K reps

print(total(pow, 2, 1000, _reps = 1000000)[0])      # 2 ** 1000, 1M reps

print(bestof(pow, 2, 100000)[0])        # 2 ** 100K, 5 dflt reps

print(bestof(pow, 2, 1000000, _reps = 30)[0])       # 2 ** 1M, best of 30

print(bestoftotal(str.upper, 'spam', _reps1 = 30, _reps = 1000))        # Best of 30, tot of 1K

print(bestof(total, str.upper, 'spam', _reps = 30))         # Nested calls work too

def spam(a, b, c, d): return a + b + c + d

print(total(spam, 1, 2, c = 3, d = 4, _reps = 1000))

print(bestof(spam, 1, 2, c = 3, d = 4, _reps = 1000))

print(bestoftotal(spam, 1, 2, c = 3, d = 4, _reps1 = 1000, _reps = 1000))

print(bestoftotal(spam, *(1, 2), _reps1 = 1000, _reps = 1000, **dict(c = 3, d = 4)))
