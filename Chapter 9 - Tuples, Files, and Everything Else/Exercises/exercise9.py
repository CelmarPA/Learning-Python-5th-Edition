S = "spam"
S = S[:1] + "l" + S[2:]  # "slam"
print(S)  # Output: "slam"

# No, you cannot use indexing alone to modify a string since strings are immutable. Indexing allows you to access characters, but it does not allow modification of individual characters. You would still need concatenation to construct the new string.
