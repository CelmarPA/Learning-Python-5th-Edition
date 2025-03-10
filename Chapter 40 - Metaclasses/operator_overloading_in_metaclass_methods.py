class A(type):
    def __getitem__(cls, i):                    # Meta method for processing classes:
        return cls.data[i]                      # Built-ins skip class, use meta
                                                # Explicit names search class + meta
class B(metaclass = A):                         # Data descriptors in meta used first
    data = 'spam'

print(B[0])                                     # Metaclass instance names: visible to class only


print(B.__getitem__)

I = B()

print(I.data, B.data)                           # Normal inheritance names: visible to instance and class

# print(I[0])                                     # ypeError: 'B' object is not subscriptable

print('-' * 80)

class A(type):
    def __getattr__(cls, name):                 # Acquired by class B getitem
        return getattr(cls.data, name)          # But not run same by built-ins

class B(metaclass = A):
    data = 'spam'

print(B.upper())

print(B.upper)

print(B.__getattr__)

I = B()

# print(I.upper)                                  # AttributeError: 'B' object has no attribute 'upper'

# print(I.__getattr__)                             # AttributeError: 'B' object has no attribute '__getattr__'.

B.data = [1, 2, 3]

B.append(4)                                     # Explicit normal names routed to meta's getattr

print(B.data)

print(B.__getitem__(0))                         # Explicit special names routed to meta's gettarr
