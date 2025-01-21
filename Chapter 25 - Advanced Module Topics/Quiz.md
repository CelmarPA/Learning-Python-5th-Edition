# Quiz Chapter 25

1. **What is significant about variables at the top level of a module whose names begin with a single underscore?**
    Variables at the top level of a module whose names begin with a single underscore are not copied out ot the importing scope when the `from *` statement form is used. They can still be accessed by an `import` or the normal `from` statement form, though. The `__all__` list is similar, but the logical converse; its contents are the only names that copied out on a `from *`.

2. **What does it mean when a module’s `__name__` variable is the string `"__main__"`?**
    If a module's `__name__` variable is string `"__main__"`, it means that the file is being executed as a top-level script instead if being imported from another file in the program. That is, the file is being used as a program, not a library.

3. **If the user interactively types the name of a module to test, how can your code import it?**
    User input usually comes into a script as a string; to import the referenced module given its string name, you can build and run and import statement with exec, or pass the string name in a call to the `__import__` or `importlib.import_module`.

4. **How is changing `sys.path` different from setting `PYTHONPATH` to modify the module search path?**
    Changing `sys.path` only affects one running program (process), and is temporary —the change goes away when the program ends. `PYTHONPATH` settings live in the operating system —they are picked up globally by all your programs on a machine, and changes to these settings endure after programs exit.

5. **If the module `__future__` allows us to import from the future, can we also import from the past?**
    No, we can't import from the past in Python. We can install (or stubbornly use) an older version of the language, but the latest Python is generally the best Python.
