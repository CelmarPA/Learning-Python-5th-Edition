# Quiz Chapter 09

1. **How can you determine how large a tuple is? Why is this tool located where it is?**
    The built-in len function returns the length for any container object in Python, including tuples. It is a built-in function instead of a type method because it applies to many different types objects.

2. **Write an expression that changes the first item in a tuple. `(4, 5, 6)` should become `(1, 5, 6)` in the process.**
    Tuples are immutable, so you can't really change tuples in place, but you can generate a new tuple with the desired value. Given T = (4, 5, 6), you can change the first item by making a new tuple form its parts by slicing and concatenating: T = (1,) + T[1:].

3. **What is the default for the processing mode argument in a file open call?**
    The default for the processing mode argument in a file open call is `r`, for reading text input.

4. **What module might you use to store Python objects in a file without converting them to strings yourself?**
    The `pickle`  module can be used to store Python object in a file without explicitly converting them to strings. The `struct` and `json` also can be used.

5. **How might you go about copying all parts of a nested structure at once?**
    Import `copy` module, and call `copy.deepcopy(X)` if you need to copy all parts of a nested structure X.

6. **When does Python consider an object true?**
    When is either a nonzero number or a nonempty collection object.

7. **What is your quest?**
    To Learn Python.
