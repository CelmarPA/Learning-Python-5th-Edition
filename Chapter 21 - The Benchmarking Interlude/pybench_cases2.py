"""
    pybench_cases.py: Run pybench on a set of pythons and statements.
    Select modes by editing this script or using command-line arguments (in
    sys.argv): e.g., run a "C:\\python27\\python pybench_cases.py" to test just
    one specific version on stmts, "pybench_cases.py -a" to test all pythons
    listed, or a "py −3 pybench_cases.py -a -t" to trace command lines too.
"""

import pybench, sys

sys.set_int_max_str_digits(300000)      # Increase the limit for integer string conversion

pythons = [         # (ispy3?, path)
    (1, 'C:\\python312\\python'),
    (0, 'C:\\python33\\python'),
    (0, 'C:\\python27\\python')
]


pythons += [
    (1, 'C:\\Pypy\\pypy310\\pypy3.10')
]


stmts = [       # (num,rpt,stmt)
    (0, 0, "[x ** 2 for x in range(1000)]"),         # Iterations
    (0, 0, "res=[]\nfor x in range(1000): res.append(x ** 2)"),         # \n=multistmt
    (0, 0, "$listif3(map(lambda x: x ** 2, range(1000)))"),   # \n\t=indent
    (0, 0, "list(x ** 2 for x in range(1000))"),         # $=list or ''
    (0, 0, "s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"),      # String ops
    (0, 0, "s = '?'\nfor i in range(10000): s += '?'"),
]

stmts += [
    # Use function calls: map wins
    (0, 0, "[ord(x) for x in 'spam' * 2500]"),
    (0, 0, "res=[]\nfor x in 'spam' * 2500: res.append(ord(x))"),
    (0, 0, "$listif3(map(ord, 'spam' * 2500))"),
    (0, 0, "list(ord(x) for x in 'spam' * 2500)"),
    # Set and dicts
    (0, 0, "{x ** 2 for x in range(1000)}"),
    (0, 0, "s=set()\nfor x in range(1000): s.add(x ** 2)"),
    (0, 0, "{x: x ** 2 for x in range(1000)}"),
    (0, 0, "d={}\nfor x in range(1000): d[x] = x ** 2"),
    # Pathological: 300k digits
    (1, 1, "len(str(2**1000000))")
] # Pypy loses on this today

tracecmd = '-t' in sys.argv         # -t: trace command lines?
pythons = pythons if '-a' in sys.argv else None         # -a: all in list, else one?
pybench.runner(stmts, pythons, tracecmd)
