# Quiz Chapter 17

1. **What is the output of the following code, and why?**

   ```python
   >>> X = 'Spam'
   >>> def func():
   ...     print(X)
   >>> func()
   ```

   The output here is `Spam`, because the function refers a global variable in the enclosing module (`X`).

2. **What is the output of this code, and why?**

   ```python
   >>> X = 'Spam'
   >>> def func():
   ...     X = 'NI!'
   >>> func()
   >>> print(X)
   ```

   The output here is `Spam` again, because the variable inside the function make it a local and effectively hides the global variable of the same name. The `print` statement finds the variable unchanged in the global (module) scope.

3. **What does this code print, and why?**

   ```python
   >>> X = 'Spam'
   >>> def func():
   ...     X = 'NI'
   ...     print(X)
   >>> func()
   >>> print(X)
   ```

   It prints `NI` on one line and `Spam`on another, because the reference to the variable  within the function finds the assigned local and the reference in the  print statement finds the global.

4. **What output does this code produce? Why?**

   ```python
   >>> X = 'Spam'
   >>> def func():
   ...     global X
   ...     X = 'NI'
   >>> func()
   >>> print(X)
   ```

   It prints `NI` because the global declaration forces the variable assigned inside the function to refer to the variable in the enclosing global scope.

5. **What about this code—what’s the output, and why?**

   ```python
   >>> X = 'Spam'
   >>> def func():
   ...     X = 'NI'
   ...     def nested():
   ...         print(X)
   ...     nested()
   >>> func()
   >>> X
   ```

   The output in this case is `NI` on one line and `Spam` on another, because the print statement in the nested function finds the name in the enclosing function's local scope, and the print at the end finds the variable in the global scope.

6. **How about this example: what is its output in Python 3.X, and why?**

   ```python
   >>> def func():
   ...     X = 'NI'
   ...     def nested():
   ...         nonlocal X
   ...         X = 'Spam'
   ...     nested()
   ...     print(X)
   >>> func()
   ```

   It prints `Spam`, because the `nonlocal` statement means that the assignment to `X` inside the nested function changes `X` in the enclosing function's local scope. Without this statement, this assignment would classify `X` as local to the nested function, making it a different variable.

7. **Name three or more ways to retain state information in a Python function.**

    Although the values of local variables go away when the function returns, you can make a Python function retain state information by using shared global variables, enclosing function scope references within nested function, or using default argument values. Function attributes can sometimes allow state to be attached to the function itself, instead of looked up in scopes. Another alternative, is using classes and OOP, sometimes supports state retention better than any of the scope-based techniques because it makes it explicit with attribute assignments.
