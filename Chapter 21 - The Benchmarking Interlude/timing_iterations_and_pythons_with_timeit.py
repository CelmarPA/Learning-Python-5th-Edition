# Interactive usage and API calls
import timeit

min(timeit.repeat(stmt = "[x ** 2 for x in range(1000)]", number = 1000, repeat = 5))
