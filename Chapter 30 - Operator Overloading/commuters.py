from commuter import Commuter1, Commuter2, Commuter3, Commuter4,  Commuter5

# Commuter1
x = Commuter1(88)
y = Commuter1(99)

print(x + 1)                                # __add__: instance + noninstance

print(1 + y)                                # __radd__: noninstance + instance

print(x + y)                                # __add__: instance + instance, triggers __radd__

# Commuter2
x = Commuter2(88)
y = Commuter2(99)

print(x + 1)

print(1 + y)

print(x + y)

# Commuter3
x = Commuter3(88)
y = Commuter3(99)

print(x + 1)

print(1 + y)

print(x + y)

# Commuter4
x = Commuter4(88)
y = Commuter4(99)

print(x + 1)

print(1 + y)

print(x + y)

# Commuter5
x = Commuter5(88)
y = Commuter5(99)

print(x + 10)                               # Result is another Commuter instance
print(10 + y)

z = x + y                                   # Not nested: doesn't recur to __radd__

print(z)
print(z + 10)
print(z + z)
print(z + z + 1)