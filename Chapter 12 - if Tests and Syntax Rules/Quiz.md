# Quiz Chapter 12

1. **How might you code a multiway branch in Python?**
    An if statement with multiple elif clauses is often the most straightforward way to do this, dictionary indexing can often achieve the same resulta, especially if the dictionary contains callable functions coded with def statements or lambda expressions.

2. **How can you code an `if/else` statement as an expression in Python?**
    The expression form Y if X else Z return Y if X is true, or Z otherwise; it's the same as a four-line if statement. The and/or combination (((X and Y) or Z)) can work the same way, but requires that the Y part be true.

3. **How can you make a single statement span many lines?**
    Wrap up the statement in an open syntactic pair ((), [], {}), and it can span as many lines as you like; the statement ends when Python sees the closing  (right) half of the pair. Backslash continuations work too, but are broadly discouraged in the Python world.

4. **What do the words `True` and `False` mean?**
    `True` and `False` are just custom versions of the integers 1 and 0, respectively: they always stand for Boolean true and false values in Python.
