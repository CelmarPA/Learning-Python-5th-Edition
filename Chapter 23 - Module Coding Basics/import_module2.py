import module2

print(module2.sys)

print(module2.name)

print(module2.func)

print(module2.klass)

print(list(module2.__dict__.keys()))

print(list(name for name in module2.__dict__.keys() if not name.startswith('__')))

print(list(name for name in module2.__dict__ if not name.startswith('__')))

print(module2.name, module2.__dict__['name'])
