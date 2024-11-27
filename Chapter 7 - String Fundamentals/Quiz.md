# Quiz Chapter 07

1. **Can the string `find` method be used to search a list?**
    No because methods are always type-specific, that is, they only work on a single data type.

2. **Can a string slice expression be used on a list?**
    Yes, unlike methods expressions are generic and apply to many types. In this case, the slice expression is really a sequence operation, that works on any type of sequence object.

3. **How would you convert a character to its ASCII integer code? How would you convert the other way, from an integer to a character?**
    The built-in `ord(S)` function converts from one-character string to an integer character code, the `char(I)` converts from the integer code back to a string.

4. **How might you go about changing a string in Python?**
    Strings cannot be changed, they are immutable, however, you can achieve similar effect by creating a new string and assigning the result back to the original variable name.

5. **Given a string `S` with the value `"s,pa,m"`, name two ways to extract the two characters in the middle.**
    You can slice the string with `S[2:4]`, or split on the comma and index teh string using `S.split(',')[1]`.

6. **How many characters are there in the string `"a\nb\x1f\000d"`?**
    Six, the string `"a\nb\x1f\000d"` contains the character `a`, new line `\n`, `b`, binary `31` (a hex escape \x1f), binary `0` (an octal escape \000), and `d`.

7. **Why might you use the `string` module instead of string method calls?**
    You should never use the string module instead of the string method calls today, it's deprecated,  and its  calls are removed completely in Python 3.X.
