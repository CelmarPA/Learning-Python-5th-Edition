class Empty:
    def __getattr__(self, attrname):            # On self.undefined
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)

X = Empty()

print(X.age)

print(X.name)