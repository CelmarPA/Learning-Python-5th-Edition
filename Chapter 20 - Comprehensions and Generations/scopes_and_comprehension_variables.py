print((X for X in range(5)))

#  print(X)         # NameError: name 'X' is not defined

X = 99

(print([X for X in range(5)]))      # 3.X: generator, set, dict, and list localize

print(X)

Y = 99

for Y in range(5): pass     # But loop statements do not localize names

print(Y)

X = 'aaa'

def func():
    Y = 'bbb'
    print(''.join(Z for Z in X + Y))        # Z comprehension, Y local, X global

func()
