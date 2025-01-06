def sumtree(l):
    tot = 0
    for x in l:     # For each item at this level
        if not isinstance(x, list):
            tot += x    # Add numbers directly
        else:
            tot += sumtree(x)       # Recur for sublists
    return tot

l = [1, [2, [3, 4], 5], 6, [7, 8]]      # Arbitrary nesting

print(sumtree(l))       # Prints 36

# Pathological cases
print(sumtree([1, [2, [3, [4, [5]]]]]))         # Prints 15 (right-heavy)
print(sumtree([[[[[1], 2], 3], 4], 5])) # Prints 15 (left-heavy)

def sumtree(l):     # Breadth-first, explicit queue
    tot = 0
    items = list(l)     # Start with copy of top level
    while items:
        front = items.pop(0)        # Fetch/delete front item
        if not isinstance(front, list):
            tot += front        # Add numbers directly
        else:
             items.extend(front)        # <== Append all in nested list
    return tot

l = [1, [2, [3, 4], 5], 6, [7, 8]]      # Arbitrary nesting

print(sumtree(l))

def sumtree(l):     # Depth-first, explicit stack
    tot = 0
    items = list(l)     # Start with copy of top level
    while items:
        front = items.pop(0)        # Fetch/delete front item
        if not isinstance(front, list):
            tot += front       # Add numbers directly
        else:
            items[:0] = front       # <== Prepend all in nested list
    return tot

l = [1, [2, [3, 4], 5], 6, [7, 8]]      # Arbitrary nesting

print(sumtree(l))
