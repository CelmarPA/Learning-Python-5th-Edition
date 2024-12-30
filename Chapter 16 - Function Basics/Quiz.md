# Quiz Chapter 14

1. **When should you use documentation strings instead of hash-mark comments?**
    Documentation strings (docstrings) are considered best for larger, functional documentation, describing the use of modules, functions, classes, and methods in your code.

2. **Name three ways you can view documentation strings.**
    You can see docstrings by printing an object's `__doc__` attribute, by passing it to PyDoc's help function, and by selecting modules in PyDoc's HTML-base user interfaces.

3. **How can you obtain a list of the available attributes in an object?**
    The built-in dir(x) function returns a list of all the attributes attached to any object. A list comprehension of the form `[a for a in dir(x) if not a.startswith('__')]` can be used to filter out internals names with underscores.

4. **How can you get a list of all available modules on your computer?**
    You can run the PyDoc's newer all-browser mode with a -b command-line switch; the top-level start page displayed in a web browser.

5. **Which Python book should you purchase after this one?**
    The books from the well known authors.
