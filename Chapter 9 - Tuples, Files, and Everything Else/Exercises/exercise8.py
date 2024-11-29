S =  "spam"
print(S[0][0][0][0][0])

# So, S[0] will give you the character at index 0, which is 's'.
# Then, when you apply another index [0] to 's' (which is a string itself), you're accessing the first character of 's'. This will result in 's' again.
# This continues with each subsequent index: each S[x] returns a string, and you can index into that string.
# Since you're repeatedly indexing into the first character of each string, the final result is 's'.

L = ['s', 'p', 'a', 'm']
print(L[0][0][0][0][0])

# L[0] would give 's', which is a single character (just like the string).
# Then, 's'[0] gives 's' (the first character of 's').
# The same pattern follows, resulting in 's'
# This indexing expression still works when applied to a list like ['s', 'p', 'a', 'm'], and the result will be 's'.

# Strings in Python are sequences of characters, and characters in Python are actually one-character strings. That's why you can continue indexing into each character (which is a string itself).

# Lists of strings work similarly. When you index a list and get an element (which can be a string), the string itself is still indexable, so the pattern continues.
