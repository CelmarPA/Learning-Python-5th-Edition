# Quiz Chapter 20

1. **What is the difference between enclosing a list comprehension in square brackets and parentheses?**
    List comprehensions in square brackets produce result list all at once in memory. But when they are enclosed in parentheses instead, they are actually generator expressions; they have a similar meaning but do not produce the result list all at once. Instead, generator expressions return a generator object, which yields one item in the result at a time when used in an iteration context.

2. **How are generators and iterators related?**
    Generators are iterable objects that support the iteration protocol automatically; they have an iterator with a `__next__` method that repeatedly advances to the next item in a series of results and raises an exception at the end of the series.

3. **How can you tell if a function is a generator function?**
    A generator function has a `yield` statement somewhere in its code. Generator functions are otherwise identical to normal functions syntactically, but they are compiled specially by Python to return an iterable generator object when called. That object retains state and code location between values.

4. **What does a yield statement do?**
    When present, this statement make Python compile the function specially as a generator; when called, the function returns a generator object that supports the iteration protocol. When the `yield` statement is run,  it sends a result back to the caller and suspends the function's state; the function can then be resumed after the last `yield` statement, in response to a `next` built-in or `__next__` method call issued by the caller.

5. **How are map calls and list comprehensions related? Compare and contrast the two.**
    The `map` call is similar to list comprehension; both produce a series of values, by collection the results of applying an operation to each item in a sequence or other iterable, one item at a time.  The primary difference it that map applies a function call to each item, and list comprehensions apply arbitrary expressions. Because of this,list comprehensions are more general; they can apply a function call expression like `map`, but `map` requires a function to apply other kind of expressions. List comprehensions also support extended syntax such as nested `for` loops and `if` clauses that subsume the `filter` built-in. `map` also differ in that it produces a generator of values; the list comprehension materializes the result list in memory all at once.
