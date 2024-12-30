S = 'Hello World!'

for charc in S:
    print(ord(charc))

sm = 0
for charc in S:
    sm += ord(charc)

print(f'The sum is: {sm}')

x = []
for c in S:
    x.append(ord(c))

print(x)

x = list(map(ord, S))
print(x)

x = [ord(c) for c in S]
print(x)
