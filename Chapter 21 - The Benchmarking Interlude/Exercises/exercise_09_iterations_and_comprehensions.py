from math import sqrt

L = [2, 4, 9, 16, 25]

# for loop

square = []
for x in L:
    square.append(sqrt(x))

print(square)

# map call

square = list(map((lambda x: sqrt(x)), L))

print(square)

# list comprehension

square = [sqrt(x) for x in L]

print(square)

# generator expression

square = (sqrt(x) for x in L)

print(list(square))
