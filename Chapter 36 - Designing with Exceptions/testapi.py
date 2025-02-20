test_list = [
    {"name": "Test 1", "result": "pass"},
    {"name": "Test 2", "result": "fail"},
    {"name": "Test 3", "result": "pass"},
    {"name": "Test 4", "result": "fail"},
]

current_test_index = 0

def moreTests():
    global current_test_index
    return current_test_index < len(test_list)

def runNextTest():
    global current_test_index
    if current_test_index >= len(test_list):
        raise Exception("No more tests to run")

    test = test_list[current_test_index]
    current_test_index += 1

    if test["result"] == "fail":
        raise Exception(f"{test['name']} failed")

def testName():
    return test_list[current_test_index - 1]["name"]
