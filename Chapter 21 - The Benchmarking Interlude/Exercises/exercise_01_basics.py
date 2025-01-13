def func(x):
    print(x)

func('spam')

func(42)

func([1, 2, 3])

func({'food': 'spam'})

# Then, try calling it without passing any argument. What happens?
#     A TypeError is raised, because the positional argument is missing

# What happens when you pass two arguments?
#     Another TypeError is raised, because the function is defined to accept only one positional argument.
