import pickle               # dumps() returns pickle string

print(pickle.dumps([1, 2, 3]))  # Python 3.X default protocol=3=binary

print(pickle.dumps([1, 2, 3], protocol=0))   # ASCII protocol 0, but still bytes!

pickle.dump([1, 2, 3], open('tmp', 'wb'))    # Always use binary in 3.X

print(open('tmp', 'r').read())

pickle.dump([1, 2, 3], open('tmp', 'wb'))

print(pickle.load(open('tmp', 'rb')))

print(open('tmp', 'rb').read())
