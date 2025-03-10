# Quiz Chapter 40

1. **What is a metaclass?**
    A metaclass is a class used to creat a class. Normal new-style classes are instances of the `type` class by default. Metaclasses are usually subclasses of the `type` class, which redefines class creation protocol methods in order to customize the class creation call issued at the end of a `class` statement; they typically redefine the methods `__new__` and `__init__` to tap into the class creation protocol. Metaclasses can also be coded other ways—as simple functions, for example—but they are always responsible for making and returning an object for the new class. Metaclasses may have methods and data to provide behavior for their classes too—and constitute a secondary pathway for inheritance search—but their attributes are accessible only to their instances, not to their instance's instances.

2. **How do you declare the metaclass of a class?**
    Use a keyword argument in the `class` header line: `class C(metaclass = M)`. The `class` header line can also name normal superclasses before the `metaclass` keyword argument.

3. **How do class decorators overlap with metaclasses for managing classes?**
    Because both are automatically triggered at the end of a `class` statement , class decorators and metaclasses can both be used to manage classes. Decorators rebind a class name to a callable's result and metaclasses route class creation through a callable, but both hooks can be used for similar purposes. To manage classes, decorators simply augment and return the original class objects. Metaclasses augment a class after they create it. Decorators may have a slight disadvantage in this role if a new class must be defined, because the original class has already been created.

4. **How do class decorators overlap with metaclasses for managing instances?**
    Because both are automatically triggered at the end of a `class` statement, we can use both class decorators and metaclasses to manage class insntances, by inserting a wrapper (proxy) object to catch instance creation calls. Decorators may rebing the class name to a callable run on instance creation that retains the original class object. Metaclasses can do the same, but may have a slight disadvantage in this role, because they must also create the class object.

5. **Would you rather count decorators or metaclasses amongst your weaponry? (And please phrase your answer in terms of a popular Monty Python skit.)**
    Our chief weapon is decorators...decorators and metaclasses...metaclasses and decorators... Our two weapons are metaclasses and decorators...and ruthless efficiency... Our three weapons are metaclasses, decorators, and ruthless efficiency... and an almost fanatical devotion to Python... Our four...no... Amongst our weapons... Amongst our weaponry...are such elements as metaclasses, decorators... I’ll come in again...
