from urllib.parse import parse_qsl


class D:
    def __get__(*args): print('get')

class C:
    a = D()                             # Attribute a is a descriptor instance

X = C()

print(X.a)                              # Runs inherited descriptor __get__

print(C.a)

X.a = 99                                # Stored on X, hiding C.a!

print(X.a)

print(list(X.__dict__.keys()))

Y = C()

print(Y.a)                              # Y still inherits descriptor

print(C.a)

print('-' * 80)

class D:
    def __get__(*args): print('get')
    def __set__(*args): raise AttributeError('cannot set')

class C:
    a = D()

X = C()

print(X.a)                              # Routed to C.a.__get__

X.a = 99                                # Routed to C.a.__set__
