def addDict(dict1, dict2):
    new = {}
    for key in dict1:
        new[key] = dict1[key]
    for key in dict2:
        new[key] = dict2[key]
    return new

x = {1: 1}
y = {2: 2}

z = addDict(x, y)

print(z)

def addTypes(x, y):
    if isinstance(x, (list, str)) and isinstance(y, (list, str)):
        return x + y

    elif isinstance(x, dict) and isinstance(y, dict):
        new = {}
        for key in x:
            new[key] = x[key]
        for key in y:
            new[key]= y[key]
        return new
    else:
        raise TypeError(f"Unsupported types for addTypes: {type(x)}, {type(y)}")
x = [1, 2]
y = [3, 4]

z = addTypes(x, y)

print(z)

x = {1: 1}
y = {2: 2}

z = addTypes(x, y)

print(z)

x = 'spam'
y = 'eggs'

z = addTypes(x, y)

print(z)
