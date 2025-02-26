class Person:
    def valid(self, value=None):
        pass

    def transform(self, value=None):
        pass

    def getName(self):
        if not self.valid():
            raise TypeError('cannot fetch name')
        else:
            return self.transform(self.name)

    def setName(self, value):
        if not self.valid(value):
            raise TypeError('cannot change name')
        else:
            self.name = self.transform(value)

person = Person()

person.getName()

person.setName('value')
