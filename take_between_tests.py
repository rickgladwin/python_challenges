import sys


def TestTakeBetween(testName, input, left, right, takeUntilEndIfRightMissing, expected):

    try:
        output = TakeBetween(input, left, right, takeUntilEndIfRightMissing)
    except:
        output = "exception"

    if output == expected or (expected is None and output == ""):
        print ("Succeeded for " + testName)
    else:
        print ("Failed for " + testName + ": Failed with [" + ("" if output is None else output) + "] rather than [" + ("" if expected is None else expected) + "]")

def Main():
    TestTakeBetween("Simple Case", "<p>Simple case</p>", "<p>", "</p>", False, "Simple case")
    TestTakeBetween("Flipped And False", "</p>Flipped<p>End", "<p>", "</p>", False, None)
    TestTakeBetween("Flipped And True", "</p>Flipped<p>End", "<p>", "</p>", True, "End")
    TestTakeBetween("Not String Ends", "Not<p>String</p>Ends", "<p>", "</p>", False, "String")
    TestTakeBetween("Matching", "Both<p>Ends<p>Match", "<p>", "<p>", False, "Ends")
    TestTakeBetween("No Left And False", "No Right</p>", "<p>", "</p>", False, None)
    TestTakeBetween("No Left And True", "No Right</p>", "<p>", "</p>", True, None)
    TestTakeBetween("No Right And False", "<p>No Right", "<p>", "</p>", False, None)
    TestTakeBetween("No Right And True", "<p>No Right", "<p>", "</p>", True, "No Right")
    TestTakeBetween("Regex Escaping", "lead (a+*)regex escape test(a+*)follow", "(a+*)", "(a+*)", False, "regex escape test")
    TestTakeBetween("Multiple", "<p><p>Multiple</p></p>", "<p>", "</p>", False, "<p>Multiple")
    TestTakeBetween("Empty Input", "", "<p>", "</p>", False, "")
    TestTakeBetween("Empty Delim", "Something", "", "", False, "exception")
    TestTakeBetween("Empty Middle", "<p></p>", "<p>", "</p>", False, "")

def TakeBetween(inStr, left, right, takeUntilEndIfRightMissing):
    # input validation
    if (
            type(inStr) is not str or
            type(left) is not str or
            type(right) is not str or
            left == '' or
            right == ''):
        raise Exception("Invalid function argument(s) sent to TakeBetween")

    left_index = inStr.find(left)
    if left_index == -1:
        return None
    start_index = left_index + len(left)
    left_onward = inStr[start_index:]

    right_index = left_onward.find(right)
    if right_index == -1:
        if takeUntilEndIfRightMissing:
            return left_onward
        else:
            return None

    return left_onward[:right_index]

Main()
