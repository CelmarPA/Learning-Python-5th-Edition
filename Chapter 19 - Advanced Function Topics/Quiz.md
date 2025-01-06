# Quiz Chapter 19

1. **How are lambda expressions and def statements related?**
   Both `lambda` and `def` create function objects to be called later. Because `lambda` is an expression, though,  it returns a function object instead of assigning it to a name, and it can be used to nest a function definition in places were a `def` will not work syntactically.

2. **What’s the point of using lambda?**
   `lambdas` allow us to "inline" small units od executable code, defer its execution, and provide it with state in the form of default arguments and enclosing scope variables. Using `lambda` is never required, you can always code a def instead and reference the function by name. `lambdas` come in handy, though, to embed small pieces of deferred code that are unlikely to be used elsewhere in a program. They commonly appear in callback-based programs such as GUIs, and they have a natural affinity with functional tools like `map` and `filter` that expect a processing function.

3. **Compare and contrast map, filter, and reduce.**
   These three built-in functions all apply another function to items in a sequence (or other iterable) object and collect results. `map` passes each item to the function and collects all results, `filter` collects items for which the function returns a `True` value, and `reduce` computes a single value by applying the function to and accumulator and successive items.

4. **What are function annotations, and how are they used?**
   Function annotations, are syntactic embellishments of a function's arguments and result, which are collected into a dictionary assigned to the function's `__annotations__` attribute. Python places no semantic meaning on these annotations, but simply packages them for potential use by other tools.

5. **What are recursive functions, and how are they used?**
   Recursive functions call themselves either directly or indirectly in order to loop. They may be used to traverse arbitrarily shaped structures, but they can also be used for iteration in general.

6. **What are some general design guidelines for coding functions?**
   Functions should generally ve small and as self-contained as possible, have a single unified purpose, and communicate with other components through input arguments and return values.

7. **Name three or more ways that functions can communicate results to a caller.**
   Functions can send back results with `return` statements, by changing passed-in mutable arguments, and by setting global variables.
