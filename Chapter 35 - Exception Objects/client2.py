import mathlib2

try:
    mathlib2.func()
except mathlib2.NumErr:
    print('caught')