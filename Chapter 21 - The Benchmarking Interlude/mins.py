# mins.py

def min1(*args):
    """Finds the smallest value using the built-in min function."""
    return min(args)

def min2(*args):
    """Finds the smallest value using a loop."""
    result = args[0]
    for value in args:
        if value < result:
            result = value
    return result

def min3(*args):
    """Finds the smallest value using recursion."""
    if len(args) == 1:
        return args[0]
    # Controle para evitar sobrecarga de recursão
    mid = len(args) // 2
    left_min = min3(*args[:mid])
    right_min = min3(*args[mid:])
    return left_min if left_min < right_min else right_min

