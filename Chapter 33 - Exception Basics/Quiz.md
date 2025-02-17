# Quiz Chapter 33

1. **Name three things that exception processing is good for.**
    Exception processing is useful for error handling, termination actions, and event notification. it can also simplify the handling of special cases and can be used to implement alternative control flows as a sort of structured 'go to' operations. In general, exception processing also cuts down on the amount of error-checking code your program may require—because all errors filter up to handlers, you may not need to test the outcome of every operation.

2. **What happens to an exception if you don’t do anything special to handle it?**
    Any uncaught exception eventually filters up to the default exception handler Python provides at the top of your program. This handler prints the familiar error message and shuts down your program.

3. **How can your script recover from an exception?**
    If you don't want the default message and shutdown, you can code `try/except` statements to catch and recover from exceptions that are raised within its nested code block. Once an exception is caught, the exception is terminated and your program continues after the `try`.

4. **Name two ways to trigger exceptions in your script.**
    The `raise` and `assert` statements can be used to trigger an exception, exactly as if it had been raised by Python itself. In principle, you can also raise an exception by making a programming mistake, but that's not usually an explicit goal!

5. **Name two ways to specify actions to be run at termination time, whether an exception occurs or not.**
    The `try/finally` statement can be used to ensure actions are run after a block of code exits, regardless of whether the block raises an exception or not. The `whit/as` statement can also be used to ensure termination actions are run, but only when processing object types that support it.
