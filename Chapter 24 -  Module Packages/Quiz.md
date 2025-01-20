# Quiz Chapter 24

1. **What is the purpose of an `__init__.py` file in a module package directory?**
    The `__init__.py` file serves to declare and initialize a regular module package. Its assigned variables become the attributes of the module object created in memory to correspond to that directory.

2. **How can you avoid repeating the full package path every time you reference a package’s content?**
    Use the `from` statement with a package to copy names out of the package directly, or use the `as` extension with the `import` statement to rename the path to a shorter synonym.

3. **Which directories require `__init__.py` files?**
    In Python 3.2 and earlier, each directory listed in an executed `import` or `from` statement must contain an `__init__.py` file.

4. **When must you use `import` instead of `from` with packages?**
    You must use `import` instead of `from` with packages only if you need to access the same name defined in more than one path. With `import` the path makes the references unique, but `from` allows only one version of any given name (unless you alse use the `as` extension to rename).

5. **What is the difference between `from mypkg import spam` and `from . import spam`?**
    In Python 3.X `from mypkg import spam` is an absolute import—the search for mypkg skips the package directory and the module is located in an absolute directory in sys.path. A statement `from . import spam`, on the other hand, is a relative import — `spam` is looked up relative to the package in which this statement is contained only.

6. **What is a namespace package?**
    A `namespace package` is an extension to the import model, available in Python 3.3 and later, that corresponds to one or more directories that do not have `__init__.py` files. When Python finds these during an import search, and does not find a simple module or regular package first, it creates a namespace package that is the virtual concatenation of all found directories having the requested module name. Further nested components are looked up in all the namespace package's directories. The effect is similar to a regular package, but content may be split across multiple directories.
