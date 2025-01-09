from timer0 import timer, cpuTimer

print(timer(pow, 2, 1000))      # Time to call pow(2, 1000) 1000 times

print(timer(str.upper, 'spam'))         # Time to call 'spam'.upper() 1000 times

print(cpuTimer(pow, 2, 1000))       # Cpu time to call pow(2, 1000) 1000000 times

print(cpuTimer(str.upper, 'spam'))      # Cpu time to call 'spam'.upper() 100000 times

import timer

print(timer.total(1000, pow, 2, 1000)[0])       # Compare to timer0 results above

print(timer.total(1000, str.upper, 'spam'))         # Returns (time, last call's result)

print(timer.bestof(1000, str.upper, 'spam'))        # 1/1000 as long as total time

print(timer.bestof(1000, pow, 2 , 1000000)[0])

print(timer.bestof(50, timer.total, 1000, str.upper, 'spam'))

print(timer.bestoftotal(50, 1000, str.upper, 'spam'))

print(min(timer.total(1000, str.upper, 'spam') for i in range(50)))

print(((((2 ** 32) / 60) / 60) / 24) / 365)         # Plus a few extra days

print(((((2 ** 32) // 60) // 60) // 24) // 365)     # Floor: see Chapter 5