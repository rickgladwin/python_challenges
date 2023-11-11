# Given a string of words delimited by spaces, reverse the
# words in string. For example, given "hello world here", return "here world hello"
#
# Follow-up: given a mutable string representation, can you perform this operation in-place?

def reverse_words(words: str) -> str:
    words_list = words.split(' ')
    # print(f'{words_list=}')
    words_list.reverse()
#     print(f'{words_list}')
    words_reversed = ' '.join(words_list)
#     print(f'{words_reversed=}')
    return words_reversed


if __name__ == '__main__':
    test_words = 'hello world'
    expected_output = 'world hello'
    result = reverse_words(test_words)

    assert result == expected_output
