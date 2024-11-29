# a. What happens when you try to use the + operator on different/mixed types
# (e.g., string + list, list + tuple)?
result = "hello" + [1, 2, 3]  # Python raises a TypeError because these types are incompatible for concatenation.

result = [1, 2, 3] + (4, 5)  # Python raises a TypeError because lists and tuples are different types.

# b. Does + work when one of the operands is a dictionary?

d1 = {'a': 1}
d2 = {'b': 2}

result = d1 + d2  # Attempting to use + with dictionaries raises a TypeError because dictionaries are not designed for direct concatenation.

# Does the append method work for both lists and strings? How about using the
# keys method on lists? (Hint: what does append assume about its subject object?)

L = [1, 2, 3]
L.append(4)
print(L)  # Output: [1, 2, 3, 4]
# In list append method works.

s = "hello"
s.append(" world")

# Append method raises an AttributeError: 'str' object has no attribute 'append'

L = [1, 2, 3]
L.keys()  # The keys method is specific to dictionaries, not lists, it raises an AttributeError: 'list' object has no attribute 'keys'

# The append method is specifically designed for mutable sequences, like lists. It assumes that the object is modifiable in-place, which is why it works with lists (which are mutable) but not with strings (which are immutable).


# d. Finally, what type of object do you get back when you slice or concatenate two
# lists or two strings?

# When you slice a list (e.g., L[start:end]), you get a new list.
# When you slice a string (e.g., s[start:end]), you get a new string.

# When you concatenate two lists (e.g., L1 + L2), you get a new list containing elements from both lists.
# When you concatenate two strings (e.g., s1 + s2), you get a new string combining the characters from both strings.
