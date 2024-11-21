# Quiz Chapter 05

1. **What is the value of the expression `2 * (3 + 4)` in Python?**
    The value will be 14, the result of 2 * 7.

2. **What is the value of the expression `2 * 3 + 4` in Python?**
    The value will be 10, the result of 6 + 4.

3. **What is the value of the expression `2 + 3 * 4` in Python?**
    The value will be 14, the result of 2 + 12.

4. **What tools can you use to find a number’s square root, as well as its square?**
    Function for obtaining the square root is available in the imported math module. To get a number's square use either the exponent expression X ** 2 or the built-in function pow(X, 2).

5. **What is the type of the result of the expression `1 + 2.0 + 3`?**
    The result will be a floating-point number, the integers are converted up to a floating point, the most complex type in the expression.

6. **How can you truncate and round a floating-point number?**
    The `int(N)` and `math.trunc(N)` functions truncate, and the `round(N, digits)` function rounds. The floor can also be compute with `math.floor(N)`, and round for display with string formatting operations.

7. **How can you convert an integer to a floating-point number?**
    The `float(I)` function converts an integer to a floating point, mixing an integer with a floating point within an expression will result in a conversion as well.

8. **How would you display an integer in octal, hexadecimal, or binary notation?**
    The `oct(I)` and `hex(I)` built-in functions return the octal and hexadecimal string forms for an integer. The `bin(I)` call also return a number's binary digits string. The % string formatting expression and `format` string method also provide targets for some such conversions.

9. **How might you convert an octal, hexadecimal, or binary string to a plain integer?**
    The `int(S, base)` function can be used to convert from octal, hexadecimal, and binary strings to a normal integers (pass in 8, 16, or 2  for the base). `eval(S)` function can bel used for this conversion too, but it's more expensive to run and can have security issues.
