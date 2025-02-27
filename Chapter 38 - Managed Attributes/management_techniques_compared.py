# Two dynamically computed attributes with properties

class Powers:
    def __init__(self, square, cube):
        self._square = square                       # _square is the base value
        self._cube = cube                           # square is the property name

    def getSquare(self):
        return self._square ** 2

    def setSquare(self, value):
        self._square = value

    square = property(getSquare, setSquare)

    def getCube(self):
        return self._cube ** 3

    cube = property(getCube)

X = Powers(3, 4)

print(X.square)                         # 3 ** 2 = 9

print(X.cube)                           # 4 ** 3 = 64

X.square = 5

print(X.square)                         # 5 ** 2 = 25

print('-' * 80)

# Same, but with descriptors (per-instance state)

class DescSquare:
    def __get__(self, instance, owner):
        return instance._square ** 2

    def __set__(self, instance, value):
        instance._square = value

class DescCube:
    def __get__(self, instance, owner):
        return instance._cube ** 3

class Powers:
    square = DescSquare()
    cube = DescCube()

    def __init__(self, square, cube):
        self._square = square                   # "self.square = square" works too,
        self._cube = cube                       # because it triggers desc __set__!

X = Powers(3, 4)

print(X.square)                                 # 3 ** 2 = 9

print(X.cube)                                   # 4 ** 3 = 64

X.square = 5

print(X.square)                                 # 5 ** 2 = 25

print('-' * 80)

# Same, but with generic __getattr__ undefined attribute interception

class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattr__(self, name):
        if name == 'square':
            return self._square ** 2
        elif name == 'cube':
            return self._cube ** 3
        else:
            raise TypeError('unknown attr: ' + name)

    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value            # Or use object
        else:
            self.__dict__[name] = value

X = Powers(3, 4)

print(X.square)                                         # 3 ** 2 = 9

print(X.cube)                                           # 4 ** 3 = 64

X.square = 5

print(X.square)                                         # 5 ** 2 = 25

print('-' * 80)

# Same, but with generic __getattribute__ all attribute interception

class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattribute__(self, name):
        if name == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif name == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == 'square':
            object.__setattr__(self, '_square', value)          # Or use __dict__
        else:
            object.__setattr__(self, name, value)

X = Powers(3, 4)

print(X.square)                                         # 3 ** 2 = 9

print(X.cube)                                           # 4 ** 3 = 64

X.square = 5

print(X.square)                                         # 5 ** 2 = 25

print('-' * 80)
