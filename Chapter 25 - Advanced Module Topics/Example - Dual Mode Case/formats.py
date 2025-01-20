#!python
"""
File: formats.py (2.X and 3.X)
Various specialized string display formatting utilities.
Test me with canned self-test or command-line arguments.
To do: add parens for negative money, add more features.
"""

def commas(n):
    """
    Format positive integer-like n for display with
    commas between digit groupings: "xxx,yyy,zzz".
    """
    digits = str(n)
    assert(digits.isdigit())
    result = ''
    while digits:
        digits, last3 = digits[:-3], digits[-3:]
        result = (last3 + ',' + result) if result else last3
    return result

def money(n, numwidth = 0, currency = '$'):
    """
    Format number n for display with commas, 2 decimal digits,
    leading $ and sign, and optional padding: "$ -xxx,yyy,zz".
    numwidth = 0 for no space padding, currency = '' to omit sumbol,
    and non-ASCII for others (e.g., pound = u'\xA3' or u'\u00A3').
    """
    sing = '-' if n < 0 else ''
    n = abs(n)
    whole = commas(int(n))
    fract = ('%.2f' % n)[-2:]
    number = '%s%s.%s' % (sing, whole, fract)
    return '%s%*s' % (currency, numwidth, number)

if __name__ == '__main__':
    def selftest():
        tests = 0,1       # fails: −1, 1.23
        tests += 12, 123, 1234, 12345, 123456, 1234567
        tests += 2 ** 32, 2 ** 100
        for test in tests:
            print(commas(test))

        print('')
        tests = 0, 1, -1, 1.23, 1., 1.2, 3.14159
        tests += 12.34, 12.344, 12.345, 12.346
        tests += 2 ** 32, (2 ** 32 + .2345)
        tests += 1.2345, 1.2, 0.2345
        tests += -1.2345, -1.2, -0.2345
        tests += -(2 ** 32), -(2 ** 32 + .2345)
        tests += (2 ** 100), -(2 ** 100)
        for test in tests:
            print('%s [%s]' % (money(test, 17), test))

    import sys
    if len(sys.argv) == 1:
        selftest()
    else:
        print(money(float(sys.argv[1]), int(sys.argv[2])))

