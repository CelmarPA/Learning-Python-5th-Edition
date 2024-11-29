L = [0, 1, 2, 3]

# a. What happens when you try to index out of bounds (e.g., L[4])?
#L[4] = 4
# IndexError:  list assignment index out of range

# What about slicing out of bounds (e.g., L[−1000:100])?
P = L[-1000:100]
# Does not raise an error, instead Python adjusts the slice to fit within the actual bounds.

# Finally, how does Python handle it if you try to extract a sequence in reverse,
# with the lower bound greater than the higher bound (e.g., L[3:1])?
print(L[3:1])
# The result is an empty list, Python slicing operates by extracting elements in a sequential order, and it does not implicitly reverse the list unless explicitly told to do so.
