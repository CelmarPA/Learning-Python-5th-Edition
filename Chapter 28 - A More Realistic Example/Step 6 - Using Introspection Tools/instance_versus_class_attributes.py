from person import Person

bob = Person('Bob Smith')

print(list(bob.__dict__.keys()))             # Instance attrs only

print(dir(bob))             # Plus inherited attrs in classes

print(len(dir(bob)))

print(list(name for name in dir(bob) if not name.startswith('__')))