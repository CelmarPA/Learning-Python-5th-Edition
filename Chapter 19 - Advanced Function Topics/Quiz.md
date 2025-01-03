# Quiz Chapter 19

1. **What is the output of the following code, and why?**

   ```python
    def func(a, b=4, c=5):
        print(a, b, c)
   
    func(1, 2)
   ```
   
    The output here is `1 2 5`, because `1` and `2` are passed to `a` and `b` by position, and `c` is omitted in the call and defaults to `5`.

2. **What is the output of this code, and why?**

   ```python
    def func(a, b, c=5):
        print(a, b, c)
   
    func(1, c=3, b=2)
   ```
   
    The output here is `1 2 3`; `1` is passed to `a` by position, and `b` and `c` are passed `2` and `3` by name.

3. **How about this code: what is its output, and why?**

   ```python
    def func(a, *pargs):
        print(a, pargs)
   
    func(1, 2, 3)
   ```
   
    This code prints `1 (2, 3)`, because `1` is passed to a and the `*pargs` collects the remaining positional arguments into a new tuple object. We can step through the extra positional arguments tuple with any iteration tool.

4. **What does this code print, and why?**

   ```python
    def func(a, **kargs):
        print(a, kargs)
   
    func(a=1, c=3, b=2)
   ```
   
    This time the code prints `1 {'c': 3, 'b': 2}`, because `1` is passed to `a` by name and the `**kargs` collects the remaining keyword arguments into a dictionary. We could step through the extra keyword arguments dictionary by key  with any iteration tool.

5. **What gets printed by this, and why?**

   ```python
    def func(a, b, c=3, d=4): print(a, b, c, d)

    func(1, *(5, 6))
   ```
   
    The output here is `1 5 6 4`; the `1` matches `a` by position, `5` and `6`, match `b` and `c` by *name positionals (`6` overrides `c`’s default), and `d` defaults to `4` because it was not passed a value.

6. **One last time: what is the output of this code, and why?**

   ```python
    def func(a, b, c): a = 2; b[0] = 'x'; c['a'] = 'y

    l=1; m=[1]; n={'a':0}
   func(l, m, n)
   l, m, n
   ```
   
    This displays `(1, ['x'], {'a': 'y'})`; the first assignment in the function doesn't impact the caller, but the second two do because they change passed-in mutable objects in place.
