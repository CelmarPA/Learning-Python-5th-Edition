class A(type):
    def a(cls):                                     # Metaclass method: gets class
        cls.x = cls.y + cls.z

class B(metaclass = A):
    y, z = 11, 22
    @classmethod                                    # Class method: gets class
    def b(cls):
        return cls.x

print(B.a())                                        # Call metaclass method; visible to class only
print(B.x)                                          # Creates class data on B, accessible to normal instances

I = B()

print(I.x, I.y, I.z)

print(I.b())                                        # Class method: sends class, not instance; visible to instance

# print(I.a())                                        # AttributeError: 'B' object has no attribute 'a'
