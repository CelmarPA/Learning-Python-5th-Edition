key = 'got'
f = {'already': (lambda: 2 + 2),
 'got':     (lambda: 2 * 4),
 'one':     (lambda: 2 ** 6)}[key]()

print(f)

# The same as:

def f1(): return 2 + 2
def f2(): return 2 * 4
def f3(): return 2 ** 6

key = 'one'
f = {'already': f1, 'got': f2, 'one': f3}[key]()

print(f)

lower = (lambda x, y: x if x < y else y)

print(lower('bb', 'aa'))
print(lower('aa', 'bb'))

import sys

showall = lambda x: list(map(sys.stdout.write, x))      # 3.X: must use list

t = showall(['spam\n', 'toast\n', 'eggs\n'])        # 3.X: can use print

showall = lambda  x: [sys.stdout.write(line) for line in x]

t = showall(('bright\n', 'side\n', 'of\n', 'life\n'))

showall = lambda x: [print(line, end='') for line in x]     # Same: 3.X only
showall = lambda x: print(*x, sep='', end='')       # Same: 3.X only