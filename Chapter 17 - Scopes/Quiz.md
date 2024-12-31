# Quiz Chapter 16

1. **What is the point of coding functions?**
    Functions are the most basic way of avoiding code redundancy in Python; factoring code into functions means that we have only one copy of an operation's code to update in the future. Functions are also the basic unit of code reuse in Python, and functions allow us to divide a complex system into manageable parts.

2. **At what time does Python create a function?**
    A function is created when Python reaches and runs the `def` statement; this statement creates a function object and assigns it the function's name.

3. **What does a function return if it has no `return` statement in it?**
    A function returns the `None` object by default if the control flow falls off the end of the function body without running into a `return` statement.

4. **When does the code nested inside the function definition statement run?**
    The function body is run when the function is later called with a call expression.

5. **What’s wrong with checking the types of objects passed into a function?**
    Checking the types of objects passed into a function effectively breaks the function's flexibility, constraining the function to work on specific types only.