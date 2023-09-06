# Write a program that computes the length of the longest common
# subsequence of three given strings. For example,
# given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious",
# it should return 5, since the longest common
# subsequence is "eieio".
import collections

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


# TODO: NOTE: consider adding the subsequence generating formula to the python_tools repo

# Recursive strategy:
# - send results to a top-level variable
# - accumulate the "list so far"
# - branch at each node, reducing the remaining index each time

class Subsequence:
    subsequences = []
    sequence = []

    def __init__(self, sequence: list):
        self.sequence = sequence

    def find_subsequences(self) -> list:
        for i in range(0, len(self.sequence)):
            self.build_subsequence(seed_sequence=[], index=i)
        return self.subsequences

    def build_subsequence(self, seed_sequence: list, index: int) -> None:
        new_seed = seed_sequence.copy()
        new_seed.append(self.sequence[index])
        self.subsequences.append(new_seed)
        if index < len(self.sequence):
            for j in range(index + 1, len(self.sequence)):
                self.build_subsequence(new_seed, j)
        return


if __name__ == '__main__':
    # test_sequence = ['a', 'b']
    # expected_result = [['a'], ['b'], ['a', 'b']]

    # test_sequence = ['a', 'b', 'c']
    # expected_result = [['a'], ['b'], ['c'], ['a', 'b'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]

    # test_sequence = ['a', 'b', 'c', 'd']
    # expected_result = [['a'], ['a', 'b'], ['a', 'b', 'c'], ['a', 'b', 'c', 'd'],
    #                    ['a', 'b', 'd'], ['a', 'c'], ['a', 'c', 'd'], ['a', 'd'], ['b'],
    #                    ['b', 'c'], ['b', 'c', 'd'], ['b', 'd'], ['c'], ['c', 'd'], ['d']]

    test_sequence = ['a', 'b', 'c', 'd', 'e']
    expected_result = [['a'], ['a', 'b'], ['a', 'b', 'c'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd', 'e'],
                       ['a', 'b', 'c', 'e'], ['a', 'b', 'd'], ['a', 'b', 'd', 'e'], ['a', 'b', 'e'],
                       ['a', 'c'], ['a', 'c', 'd'], ['a', 'c', 'd', 'e'], ['a', 'c', 'e'], ['a', 'd'],
                       ['a', 'd', 'e'], ['a', 'e'], ['b'], ['b', 'c'], ['b', 'c', 'd'], ['b', 'c', 'd', 'e'],
                       ['b', 'c', 'e'], ['b', 'd'], ['b', 'd', 'e'], ['b', 'e'], ['c'], ['c', 'd'],
                       ['c', 'd', 'e'], ['c', 'e'], ['d'], ['d', 'e'], ['e']]

    print(f'test_sequence: {test_sequence}')
    result = Subsequence(test_sequence).find_subsequences()
    print(f'result: {result}')
    # assert collections.Counter(result) == collections.Counter(expected_result)
    # TODO: create deep compare function for nested lists
