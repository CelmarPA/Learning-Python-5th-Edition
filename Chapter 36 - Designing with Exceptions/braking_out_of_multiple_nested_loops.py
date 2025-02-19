class ExitLoop(Exception): pass

try:
    while True:
        while True:
            for i in range(10):
                if i > 3: raise ExitLoop                    # break exits just one level
                print('loop3: %s' % i)
            print('loop2')
        print('loop1')
except ExitLoop:
    print('continuing')                                     # Or just pass, to move on

print(i)
