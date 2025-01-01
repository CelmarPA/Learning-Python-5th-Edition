def tester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested

F = tester(0)
F('spam')
F('ham')
print(F.state)

G = tester(42)
G('eggs')

F('ham')

print(F.state)
print(G.state)

print(F is G)
