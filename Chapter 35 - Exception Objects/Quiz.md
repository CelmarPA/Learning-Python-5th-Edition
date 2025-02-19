# Quiz Chapter 35

1. **What are the two new constraints on user-defined exceptions in Python 3.X?**
    In 3.X, classes must define exceptions (that is, a class instance object is raised and caught). In addition, exception classes must be derived form the built-in class `BaseException`; most programs inherit from its `Exception` subclass, to support catchall handlers for normal kinds of exceptions.

2. **How are raised class-based exceptions matched to handlers?**
    Class-based exceptions match by superclass relationship: naming a superclass in an exception handler will catch instances of that class, as well as instances of any of its subclasses lower in the class tree. Because of this, you can think of superclasses as general exception categories and subclasses as more specific types of exceptions within those categories.

3. **Name two ways that you can attach context information to exception objects.**
    You can attach context information to class-based exceptions by filling out instance attributes in the instance object raised, usually in a custom class constructor. For simpler needs, built-in exception superclasses provide a constructor that stores its arguments ont he instance automatically (as a tuple in the attribute args). In exception handlers, you list a variable to be assigned to the raised instance, then go through this name to access attached state information and call any methods defined in the class.

4. **Name two ways that you can specify the error message text for exception objects.**
    The error message text in class-based exceptions can be specified with a custom `__str__` operator overloading method. For simpler needs, built-in exception superclasses automatically display anything you pass to the class constructor. Operations like `print` and `str` automatically fetch the display string of an exception object when it is printed either explicitly or as part an error message.

5. **Why should you not use string-based exceptions anymore today?**
    Because Guido said so—they have been removed as of both Python 2.6 and 3.0. There are arguably good reasons for this: string-based exceptions did not support categories, state information, or behavior inheritance in the way class-based exceptions do. In practise, this made string-based exceptions easier to use at first when programs were small, but more complex to use as programs grew larger.
