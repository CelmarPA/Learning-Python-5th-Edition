# Quiz Chapter 26

1. **What is the main point of OOP in Python?**
    OOP is about code reuse—you factor code to minimize redundancy and program by customizing what already exists instead of changing code in place or starting from scratch.

2. **Where does an inheritance search look for an attribute?**
    An inheritance search looks for an attribute first in the instance object, then in the class the instance was created from, then in all higher superclasses, progressing from the bottom to the top of the object tree, and from left to right (by default).

3. **What is the difference between a class object and an instance object?**
    Both class and instance objects are namespace (packages of variables that appear as attributes). The main difference between them is that classes are a kind of factory for creating multiple instances. Classes also support operator overloading methods, which instances inherit, and treat any functions nested in the class as methods for processing instances.

4. **Why is the first argument in a class’s method function special?**
    The first argument in a class's method function is special because it always receives the instance object that is the implied subject of the method call. It's usually called `self` by convention. Because method functions always have this implied subject and object context by default.

5. **What is the `__init__` method used for?**
    If the `__init__` method is coded or inherited in a class, Python calls it automatically each time and instance of that class is created. It's known as the constructor method; it is passed the new instance implicitly, as well as any arguments passed explicitly to the class name. It's also the most commonly used operator overloading method. If no `__init__` method is presented, instances simply begin life as empty namespaces.

6. **How do you create a class instance?**
    You create a class instance by calling the class name as though it were a function; any arguments passed into the clas name show up´as arguments two and beyond in the `__init__` constructor method. The new instance remembers the class it was created from for inheritance purpose.

7. **How do you create a class?**
    You create a class by running a class statement; like function definitions, these statements normally run when the enclosing module file is imported.

8. **How do you specify a class’s superclasses?**
    You specify a class's superclass by listing them in parentheses in the class statement, after the new class's name. The left-to right order in which the classes are listed in the parentheses gives the left-to-right inheritance search order in the class tree.
