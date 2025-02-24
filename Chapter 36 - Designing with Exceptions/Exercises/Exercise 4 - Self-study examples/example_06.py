# Test for regressions in the output of a set of scripts

import os

testScripts = [dict(script = 'test1.py', args = ''),            # Or glob script/args dir
               dict(script = 'test2.py', args = 'spam')]

for testCase in testScripts:
    commandLine = '%(script)s %(args)s' % testCase
    output = os.popen(commandLine).read()
    print(output)
    result = testCase['script'] + '.result'

    if not os.path.exists(result):
        open(result, 'w').write(output)
        print('Created:', result)
    else:
        priorResult = open(result).read()
        if output != priorResult:
            print('FAILED:', testCase['script'])
            print(output)
        else:
            print('Passed:', testCase['script'])
