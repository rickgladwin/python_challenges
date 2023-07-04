# Write a program that computes the length of the longest common
# subsequence of three given strings. For example,
# given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious",
# it should return 5, since the longest common
# subsequence is "eieio".
from numpy import str_

# Strategy:
# - eliminate non-common elements
# - explore all possible subsequences for the shortest string, recording common subsequences
#  from the other strings
# - select the largest result (if any), return its length (or zero)

string_1 = 'epidemiologist'
string_2 = 'refrigeration'
string_3 = 'supercalifragilisticexpialodocious'

str_1_set = set(string_1)
str_2_set = set(string_2)
str_3_set = set(string_3)
print(f'str_1_set: {str_1_set}')
print(f'str_2_set: {str_2_set}')
print(f'str_3_set: {str_3_set}')
common_chars = str_1_set.intersection(str_2_set.intersection(str_3_set))
print(f'common_chars: {common_chars}')
str_1_reduced = [x for x in list(string_1) if x in common_chars]
print(f'str_1_reduced: {str_1_reduced}')

str_2_reduced = [x for x in list(string_2) if x in common_chars]
print(f'str_2_reduced: {str_2_reduced}')

str_3_reduced = [x for x in list(string_3) if x in common_chars]
print(f'str_3_reduced: {str_3_reduced}')

# TODO: find a recursive function that will explore the tree of sequences
#  Consider starting from the end of the list (or end - 1) and appending
#  each remaining element in order to form each new branch.
#  NOTE: the algorithm will be similar to the one for finding combinations
#  NOTE: consider adding the resulting formula to the python_tools repo


def subsequences(sequence: list) -> list:
    # handle sequences of length 1
    if len(sequence) == 1:
        return [sequence]
    # handle sequences of length 2
    result = []
    for i in range(0, len(sequence)):
        result.append([sequence[i]])
    for j in range(0, len(result) - 1):
        clone = result[j].copy()
        print(f'\n--- clone: {clone}')
        print(f'sequence[j + 1]: {sequence[j + 1]}')
        clone.append(sequence[j + 1])
        result.append(clone)
    return result

    # get subsequences of length 1, store them
    # for x in sequence:
    #     result.append(x)
    # get subsequences of length 2, concat with stored, store them

    # ...
    # get subsequences of length len(sequence), concat with stored, store them
    # return all stored




if __name__ == '__main__':
    test_sequence = ['a', 'b']
    expected_result = [['a'], ['b'], ['a', 'b']]
    result = subsequences(test_sequence)
    print(f'result: {result}')
    assert result == expected_result
