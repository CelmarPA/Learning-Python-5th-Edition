class MyBad(Exception): pass

try:
    raise MyBad('Sorry--my mistake!')
except MyBad as X:
    print(X)

# raise MyBad('Sorry--my mistake!')

class MyBad(Exception):
    def __str__(self):
        return 'Always look on the bright side of life...'

try:
    raise  MyBad()
except MyBad as X:
    print(X)

# raise MyBad()
