class C: pass
class D: pass

c, d = C(), D()

print(type(c) == type(d))           # 3.X: compares the instances' classes

print(type(c), type(d))

print(c.__class__, d.__class__)

c1, c2 = C(), C()

print(type(c1) == type(c2))
