# Quiz Chapter 29

1. **What is an abstract superclass?**
    An abstract superclass is a class that call a method, but does not inherit of define it—it expects the method to be filled in by a subclass. This is often used as a way to generalize classes when behavior cannot be predicted until a more specific subclass is coded. OOP frameworks also use this as a way to dispatch to client-defined, customizable operations.

2. **What happens when a simple assignment statement appears at the top level of a class statement?**
    When a simple assignment statement (X = Y) appears at the top level of a `class` statement, it attaches a data attribute to the class (`Class.X`). Like all class attributes, this will be shared by all instances; data attributes are not callable method functions, though.

3. **Why might a class need to manually call the `__init__` method in a superclass?**
    A class must manually call the `__init__` method in a superclass if it defines an `__init__` constructor of its own and still wants the superclass's constructor code to run. Python itself automatically runs just one constructor—the lowest one in the tree. Superclass constructors are usually called through the class name, passing in the `self` instance manually: `Superclass.__init__(self,...)`.

4. **How can you augment, instead of completely replacing, an inherited method?**
    To augment instead of completely replacing an inherited method, redefine it in a subclass, but call back to the superclass's version of the method manually from the new version of the method in the subclass. That is, pass the `self` instance to the superclass's version of the method manually: `Superclass.method(self,...)`.

5. **How does a class’s local scope differ from that of a function?**
    A class is a local scope and has access to enclosing local scopes, but it does not serve as an enclosing local scope to further nested code. Like modules, the class local scope morphs into an attribute namespace after the class statement is run.

6. **What...was the capital of Assyria?**
    Ashur (or Qalāt Sherqat), Calah (or Nimrud), the short-lived Dur Sharrukin (or Khorsabad), and finally Nineveh.
