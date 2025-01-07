print(open('myfile').readlines())

print([line.rstrip() for line in open('myfile').readlines()])

print([line.rstrip() for line in open('myfile')])

print(list(map((lambda line: line.rstrip()), open('myfile'))))

listoftuple = [('bob', 35, 'mgr'), ('sue', 40, 'dev')]

print([age for (name, age, job) in listoftuple])

print(list(map((lambda x: x[1]), listoftuple)))
