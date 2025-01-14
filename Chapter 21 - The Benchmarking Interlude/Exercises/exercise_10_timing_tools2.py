def dictComp(j):
    return {i: i for i in range(j)}

def dictLoop(j):
    new = {}
    for i in range(j): new[i] = i
    return new

print(dictComp(10))

print(dictLoop(10))

from timer2 import total, bestof

print(bestof(dictComp, 10000)[0])       # 10,000-item dict

print(bestof(dictLoop, 10000)[0])

print(bestof(dictComp, 100000)[0])      # 100,000-items: 10X slower

print(bestof(dictLoop, 100000)[0])

print(bestof(dictComp, 1000000)[0])      # 1 of 1M-items: 10X time

print(bestof(dictLoop, 1000000)[0])

print(total(dictComp, 1000000, _reps = 50)[0])      # Total to make 50 1M-item dicts

print(total(dictLoop, 1000000, _reps = 50)[0])
