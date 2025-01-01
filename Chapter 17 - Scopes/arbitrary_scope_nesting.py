def f1():
    x = 99
    def f2():
        def f3():
            print(x)        # Found in f1's local scope!
        f3()
    f2()

f1()
