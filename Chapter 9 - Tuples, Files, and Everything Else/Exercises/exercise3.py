L = [0, 1, 2, 3]
L[2] = []
# Assigning an empty list to a specific offset replaces the item at that position with an empty list.
print(L)
L[2:3] = []
# Assigning an empty list to a slice deletes the slice entirely from the list.
