"""
y = 2

x = y // 2      # For some y > 1

while x > 1:
    if y % x == 0:      # Remainder
        print(y, 'has factor', x)
        break       # Skip else
    x -= 1
else:       # Normal exit
    print(y, 'is prime')
"""

def prime(y):
    if y <= 1:      # For some y > 1
        print(y, 'not prime')
    else:
        x = y // 2
        while x > 1:
            if y % x == 0:      # No remainder?
                print(y, 'has factor', x)
                break       # Skip else
            x -= 1
        else:
            print(y, 'is prime')

prime(15); prime(13.0)

prime(15);  prime(15.0)

prime(3); prime(2)

prime(1); prime(-3)

# optimized

def primes(y):
    if y <= 1:      # For numbers less than or equal to 1
        print(f'{y} not prime')
    elif isinstance(y, float):
        print(f'{y} => float numbers not prime')
    else:
        for x in range(y // 2, 1, -1):       # Loop from y // 2 down to 2
            if y % x == 0:      # Check if x is a factor of y
                print(f'{y} has factor {x}')
                break       # Skip else
        else:
            print(f'{y} is prime')

primes(15); primes(13.0)

primes(15);  primes(15.0)

primes(3); primes(2)

primes(1); primes(-3)

import timeit


# Test with a large prime number
y = 10007  # Large prime number for benchmarking

# Time the functions
time_primes = timeit.timeit(lambda: primes(y), number=10000)
time_prime = timeit.timeit(lambda: prime(y), number=10000)

print(f'Time for primes (for loop): {time_primes:.5f} seconds')
print(f'Time for prime (while loop): {time_prime:.5f} seconds')

"""
    If floor division (y // 2) is replaced by true division (y / 2) the code will no 
    longer correctly evaluate the factor of the numbers, generating an error and incorrectly
    defining the prime numbers.
"""
