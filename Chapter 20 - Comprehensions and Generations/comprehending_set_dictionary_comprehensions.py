from tkinter import Listbox

print({x * x for x in range(10)})       # Comprehension

print(set(x * x for x in range(10)))       # Generator and type name

print({x: x * x for x in range(10)})

print(dict((x, x * x) for x in range(10)))

# print(x)        # name 'x' is not defined

res = set()

for x in range(10):
    res.add(x * x)

print(res)

res = {}

for x in range(10):         # Dict comprehension equivalent
    res[x] = x * x

print(res)

print(x)      # Localized in comprehension expressions, but not in loop statements

G = ((x, x * x) for x in range(10))

print(next(G))

print(next(G))
