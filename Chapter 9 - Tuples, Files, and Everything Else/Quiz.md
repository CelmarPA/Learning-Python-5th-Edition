# Quiz Chapter 08

1. **Name two ways to build a list containing five integer zeros.**
    A literal expression like [0, 0, 0, 0, 0] and a repetition expression like [0] * 5, will each create a list of five zeros.

2. **Name two ways to build a dictionary with two keys, `'a'` and `'b'`, each having an associated value of `0`.**
    A literal expression like {'a': 0, 'b': 0} or a series of assignments like Dict = {}, Dict[`'a'`] = 0, Dict[`'b'`] = 0, or you can also use the newer dict(a=0, b=0) keyword form.

3. **Name four operations that change a list object in place.**
    The `append` and `extend` methods grow a list in place, the `sort`, `reverse` methods order and reverse lists.

4. **Name four operations that change a dictionary object in place.**
    Assignment to a new or existing key, which creates or changes the key's entry in the table. The `del` statement deletes a key's entry, `update` method merges on dictionary into another in place, and `pop` method removes a key and returns the value it had.

5. **Why might you use a dictionary instead of a list?**
    Dictionaries are generally better when the data is labeled; lists are best suited to collections of unlabeled items. The lookup of dictionary is also usually quicker than searching a list, though this might vary per program.
