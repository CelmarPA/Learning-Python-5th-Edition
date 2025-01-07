print([x for x in range(5) if x % 2 == 0])

print(list(filter((lambda x: x % 2 == 0), range(5))))

res = []
for x in range(5):
    if x % 2 == 0:
        res.append(x)

print(res)

print([x ** 2 for x in range(10) if x % 2 == 0])

print(list( map((lambda x: x ** 2), filter((lambda x: x % 2 == 0), range(10)))))
