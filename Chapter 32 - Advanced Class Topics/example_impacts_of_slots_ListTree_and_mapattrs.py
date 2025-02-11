from listtree import ListTree

class C(ListTree): pass

X = C()                             # OK: no __slots__ used

print(X)

class C(ListTree): __slots__ = ['a', 'b']           # OK: superclass produces __dict_

X = C()

X.c = 3

print(X)                            # Displays c at X, a and b at C

class A: __slots__ = ['a']          # Both OK by bullet 1 above

class B(A, ListTree): pass

class A: __slots__ = ['a']

class B(A, ListTree): __slots__ = ['b']     # Displays b at B, a at A
