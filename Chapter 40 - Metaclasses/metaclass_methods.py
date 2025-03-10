class A(type):
    def x(cls): print('ax', cls)                    # A metaclass (instances=classes)
    def y(cls): print('ay', cls)                    # y is overridden by instance B

class B(metaclass = A):
    def y(self): print('by', self)                  # A normal class (normal instances)
    def z(self): print('bz', self)                  # Namespace dict holds y and z

print(B.x)                                          # x acquired from metaclass

print(B.y)                                          # y and z defined in class itself

print(B.z)

B.x()                                               # Metaclass method call: gets cls

I = B()

I.y()

I.z()

# I.x()                                               # AttributeError: 'B' object has no attribute 'x'
