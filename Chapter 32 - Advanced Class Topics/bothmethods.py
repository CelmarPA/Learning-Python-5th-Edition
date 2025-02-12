class Methods:
    def imeth(self, x):                 # Normal instance method: passed a self
        print([self, x])

    def smeth(x):                       # Static: no instance passed
        print([x])

    def cmeth(cls, x):                  # Class: gets class, not instance
        print([cls, x])

    smeth = staticmethod(smeth)         # Make smeth a static method (or @: ahead)
    cmeth = classmethod(cmeth)          # Make cmeth a class method (or @: ahead)

obj = Methods()                         # Callable through instance or class

obj.imeth(1)

Methods.imeth(obj, 2)

Methods.smeth(3)                        # Static method: call through class. No instance passed or expected

obj.smeth(4)                            # Static method: call through instance. Instance isn't passed

Methods.cmeth(5)                        # Class method: call through class. Becomes cmeth(Methods, 5)

obj.cmeth(6)                            # Class method: call through instance. Becomes cmeth(Methods, 6)
