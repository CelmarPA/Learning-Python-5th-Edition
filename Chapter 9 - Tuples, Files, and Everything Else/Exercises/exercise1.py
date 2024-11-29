print(2 ** 16)      # 2 to the power of 16
print(2 / 5, 2 / 5.0)       # int 2 divide by int 5, int 2 divide by float 5.0

print("spam" + "eggs")      # concatenate two strings

S = "ham"
print("eggs" + S)       # concatenate two strings
print(S * 5)        # repetition
print(S[:0])        # slice, creating an empty string

print("green %s and %s" % ("eggs", S))      # formatting with %
print('green {0} and {1}'.format('eggs', S)) # formatting with expression

print(('x',)[0]) # tuple with single expression
print(('x', 'y')[1]) # indexing a tuple

L = [1, 2, 3] + [4, 5, 6]       # list concatenate
print(L)
print(L, L[:], L[:0], L[-2], L[-2:])        # indexing list
print(([1, 2, 3] + [4, 5, 6])[2:4])     # list concatenate and indexing
L.reverse()
print(L)       # reverse a list
L.sort()
print(L) # sorting list
print(L.index(4)) # get index of int

print({'a': 1, 'b': 2}['b'])

D = {'x': 1, 'y': 2, 'z': 3}        # creating a dictionary

D['w'] = 0      # assigning 0 to a new key
print(D['x'] + D['w'])      # addition 1 + 0
D[(1,2,3)] = 4      # assigning 4 to a tuple-key
print(list(D.keys()), list(D.values()), (1,2,3) in D)       # prints list of keys and values of D and print test in

L = [[]], ["",[],(),{},None]        # a tuple with empties list, dict and tuple inside
