# Search the string for first occurrence of left, and then take all characters until
#  right is found. Result excludes those bounding substrings.
# If left isn't found (or right isn't found and takeUntilEndIfRightMissing is off), it returns null.
#
# string TakeBetween(string input, string left, string right, bool takeUntilEndIfRightMissing)
#
# Example:
#
# TakeBetween("<p>My paragraph</p>", "<p>", "</p>", true) returns "My paragraph".

def take_between(inStr: str, left: str, right: str, takeUntilEndIfRightMissing: bool) -> str | None:
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


if __name__ == '__main__':
    test_haystack = '''<p>My paragraph</p>
<p>
</p>
0
'''
    test_haystack_2 = '''<p>My paragraph
<p>
asdf
0
'''
    test_haystack_3 = '<p>First instance only</p><p>Ignore remaining</p>'
    test_haystack_4 = '<p>First instance only</p><p>Ignore remaining</p>'
    test_haystack_5 = ''

    # print(take_between(inStr=test_haystack, left='<p>', right='</p>', takeUntilEndIfRightMissing=True))
    # print(take_between(inStr=test_haystack_2, left='<p>', right='</p>', takeUntilEndIfRightMissing=True))
    # print(take_between(inStr=test_haystack_3, left='<p>', right='</p>', takeUntilEndIfRightMissing=False))
    # print(take_between(inStr=test_haystack_4, left='', right='</p>', takeUntilEndIfRightMissing=False))
    print(take_between(inStr='', left='<p>', right='</p>', takeUntilEndIfRightMissing=False))
    # print(take_between(inStr=test_haystack_4, left='', right='', takeUntilEndIfRightMissing=False))
