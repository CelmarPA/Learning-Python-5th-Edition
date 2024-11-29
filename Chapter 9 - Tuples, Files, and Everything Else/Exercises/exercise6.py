D = {'a': None, 'b': None, 'c': None}
print(D['d'])
D['d'] = 'spam'

# If you try to access a key that does not exist in the dictionary, Python raises a KeyError because the key is not found.
# Different of list out-of-bounds, a new key is created and the string 'spam' is assign to it.
