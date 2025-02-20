import sys

log = open('testlog', 'a')

from testapi  import moreTests, runNextTest, testName

def testdriver():
    while moreTests():
        try:
            runNextTest()
        except:
            print('FAILED', testName(), sys.exc_info()[:2], file = log)
        else:
            print('PASSED', testName(), file = log)

testdriver()
