# Quiz Chapter 31

1. **What is multiple inheritance?**
    Multiple inheritance occurs when a class inherits from more than one superclass; it's useful for mixing together multiple packages of class-based code. The left-to-right order in `class` statement headers determines the general order of attribute searches.

2. **What is delegation?**
    Delegation involves wrapping an object in a proxy class, which adds extra behavior and passes other operations to the wrapped object. The proxy retains the interface of the wrapped object.

3. **What is composition?**
    Composition is a technique whereby a controller class embeds and directs a number of objects, and provides an interface all its own; it's a way to build up larger structures with classes.

4. **What are bound methods?**
    Bound methods combine an instance and a method function; you can call them without passing in an instance object explicitly because the original instance is still available.

5. **What are pseudoprivate attributes used for?**
    Pseudoprivate attributes (whose names begin but do not end with two leading underscores: __X) are used to localize name to the enclosing class. This includes both class attributes like methods defined inside the class, and `self` instance attributes assigned inside the class's methods. Such names are expanded to include the class name, which makes them generally unique.
