# Quiz Chapter 21

1. **What conclusions can you draw from this chapter about the relative speed of Python iteration tools?**
    `List comprehensions` are often quickest of the bunch; `map` beats list comprehensions in Python only when tools must call functions, `for` loops are slower than comprehensions by a constant factor. Under PyPy, some of these findings differ; `map` often turns in a different relative performance, for example, and list comprehensions seem always quickest, perhaps due to function-level optimizations.

2. **What conclusions can you draw from this chapter about the relative speed of the Pythons timed?**
    PyPy 1.9 is typically faster than CPython 2.7, and CPython 2.7 is often faster than Cpython 3.3. In most cases times, PyPy is some 10X faster than CPython, and CPython 2.7 is often a small constant faster than CPython 3.3. In cases that use integer math, CPython 2.7 can be 10X faster than CPython 3.3, abd PyPy can be 100X faster than 3.3. In other cases  (e.g., string operations and file iterators), PyPy can be slower than CPython by 10X, though `timeit` and memory management differences may influence some results.
