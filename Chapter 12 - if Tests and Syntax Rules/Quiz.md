# Quiz Chapter 11

1. **Name three ways that you can assign three variables to the same value.**
    Multiple-target assignments (A = B = C = 0), sequence assignment (A, B, C = 0, 0, 0), or multiple assignment statements on three separate lines (A = 0, B = 0, C = 0).

2. **Why might you need to care when assigning three variables to a mutable object?**
    If you assign them this way: A = B = C = [], all three names reference the same object, so changing it in place from one (e.g., A.append(99)) will affect the others. This happens only for in-place changes to mutable objects.

3. **What’s wrong with saying `L = L.sort()`?**
    The list `sort` method is like `append` in that it makes an in-place change to the subject list; it returns `None`, not the list it changes.

4. **How might you use the `print` operation to send text to an external file?**
    To print to a file for a single print operation, you can use 3.X's (print(X, file=F)) call form.
