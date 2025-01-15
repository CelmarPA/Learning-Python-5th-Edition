# Quiz Chapter 23

1. **How do you make a module?**
    To create a module, you simply write a text file containing Python statements; every source code file is automatically a module, and there is no syntax for declaring one.

2. **How is the `from` statement related to the `import` statement?**
    The `from` statement imports an entire module, like the `import` statement, but as an extra step it also copies one or more variables from the imported module into the scope where the `from` appears.

3. **How is the `reload` function related to imports?**
    By default, a module is imported only once per process. The `reload` function forces a module to be imported again. It is mostly used to pick up a new version of a module's source code during development and dynamic customization scenarios.

4. **When must you use `import` instead of `from`?**
    You must use `import` instead of `from` only when you need to access the same name in two different modules; because you'll have to specify the names of the enclosing modules, the two names will be unique.

5. **Name three potential pitfalls of the `from` statement.**
    The `from` statement can obscure the meaning of a variable, can have problems with reload call, and can corrupt namespaces. The `from *` form is worse in most regards; it can seriously corrupt namespaces and obscure the meaning of variables, so it is probably best used sparingly.

6. **What...is the airspeed velocity of an unladen swallow?**
    An African or European swallow? lol
