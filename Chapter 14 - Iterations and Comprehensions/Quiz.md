# Quiz Chapter 14

1. **How are `for` loops and iterable objects related?**
    The `for` loop uses the iteration protocol to step through items in the iterable object across which it is iterating. It first fetches an iterator from the iterable by passing the object to iter, and then calls this iterator object’s `__next__` method in 3.X on each iteration and catches the StopIteration exception to determine when to stop looping.

2. **How are `for` loops and list comprehensions related?**
    Both are iteration tools and contexts. List comprehensions are a concise and often efficient way to perform a common `for`loop task.

3. **Name four iteration contexts in the Python language.**
    `for`loop, list comprehension, the `map` built-in function, the `in` membership test expression, list and tuple.

4. **What is the best way to read line by line from a text file today?**
    The best way to read lines from a text file today is to not read it explicitly at all, instead, open the file within an iteration context tool such as a `for` loop or list comprehension, and let the iteration tool automatically scan one line at a time.

5. **What sort of weapons would you expect to see employed by the Spanish Inquisition?**
    A little bayonet.
