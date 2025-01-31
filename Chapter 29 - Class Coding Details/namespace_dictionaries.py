class Super:
    def hello(self):
        self.data1 = 'spam'

class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'

X = Sub()

print(X.__dict__)                   # Instance namespace dict

print(X.__class__)                  # Class of instance

print(Sub.__bases__)                # Superclasses of class

print(Super.__bases__)              # () empty tuple in Python 2.X

Y = Sub()

X.hello()

print(X.__dict__)

X.hola()

print(X.__dict__)

print(list(Sub.__dict__.keys()))

print(list(Super.__dict__.keys()))

print(Y.__dict__)

print(X.data1, X.__dict__['data1'])

X.data3 = 'toast'

print(X.__dict__)

X.__dict__['data3'] = 'ham'

print(X.data3)
