class Methods(object):                              # object needed in 2.X for property setters
    def imeth(self, x):                             # Normal instance method: passed a self
        print([self, x])

    @staticmethod
    def smeth(x):                                   # Static: no instance passed
        print([x])

    @classmethod
    def cmeth(cls, x):                              # Static: no instance passed
        print(cls, x)

    @property
    def name(self):                                 # Property: computed on fetch
        return 'Bob ' + self.__class__.__name__

obj = Methods()

obj.imeth(1)

obj.smeth(2)

obj.cmeth(3)

print(obj.name)
