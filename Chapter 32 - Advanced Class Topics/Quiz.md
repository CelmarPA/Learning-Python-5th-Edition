# Quiz Chapter 31

1. **Name two ways to extend a built-in object type.**
    You can embed a built-in object in a wrapper class, or subclass the built-in type directly. The latter approach tends to be simpler, as most original behavior is automatically inherited.

2. **What are function and class decorators used for?**
    Functions decorators are generally used to manage a function or method, or add to it a layer of logic that is run each time the function or method is called. They can be used to log or count calls to a function, check its argument types, and so on. They are also used to "declare" static methods (simple functions in a class that are not passed an instance when called), as well as class methods and properties. Class decorators ara similar, but manage whole objects and their interfaces instead of a function call.

3. **How do you code a new-style class?**
    New-style classes are coded by inheriting from the `object` built-in class (or any other built-in type).

4. **How are new-style and classic classes different?**
    New-style classes search the diamond pattern of multiple inheritance trees differently—they essentially search breadth-first (across), instead of depth-first (up) in diamond trees. New-style classes also change the result of the `type` built-in for instances and classes, do not run generic attribute fetch methods such as `__getattr__` for built-in operation methods, and support a set of advanced extra tools including properties, descriptors, `super`, and `__slots__` instance attribute lists.

5. **How are normal and static methods different?**
    Normal (instance) methods receive a `self` argument (the implied instance), but static methods do not. Static methods are simple functions nested in class objects. To make a method static, it must either be run through a special built-in function or be decorated with decorator syntax.

6. **Are tools like `__slots__` and `super` valid to use in your code?**
    Of course, but you shouldn't use advanced tools automatically without carefully considering their implications. Slots, for example, can break code; `super` can mask later problems when used for single inheritance, and in multiple inheritance brings with it substantial complexity for an isolated use case; and both require universal deployment to be most useful. Evaluating new or advanced tools is a primary task of any engineer.

7. **How long should you wait before lobbing a “Holy Hand Grenade”?**
    Three seconds.