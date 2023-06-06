# Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.
# For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true,
#  since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.
# Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up
#  into two subsets that add up to the same sum.
#
# Strategy:
# - Generate all possible permutations of 2 subsets
#  - generate the permutations
#  - run the breakpoint from {1|N-1} to {N-1|1}
# - Compare the sums of the subsets
# - If the sums are equal, return True
# - If loop ends, return False
#
# Optimizations:
# - rather than compare the sums of the split permutation each time, add and subtract from a pair of
#  sums as the divider is moved.
# - We can stop on the first match, so try and find a match earlier:
#  - start at the middle (do this for all permutations as a way to hit the solution faster,
#    assuming a normal distribution)
#    - assume a normal distribution with low probability of outliers
#    - start the divider at the middle of the list
#    - move the divider first one way, then the other
#  - sort and guess (not exhaustive, but might be faster depending on the distribution):
#    - sort the original list
#    - assume a normal distribution, and start the divider at sqrt(N)/N from the left index
#    - move the divider one way. If the sums get closer, keep moving that way.
#      If they get further apart, move the other way. Stop when the sums are equal, the difference has
#      decreased and then increased, or the divider reaches the end of the list.

from itertools import permutations
from math import factorial as fact
import random


def list_has_equal_sums(numbers: list[int]) -> bool:
    n: int = len(numbers)
    perms = permutations(numbers, n)
    # print(f'perms: {perms}')
    # print(f'number of permutations = n! / (n-r)! = n! = {fact(n)}')
    for perm in perms:
        print(f'\n--- trying perm: {perm}')
        print(f'type(perm): {type(perm)}')
        if perm_has_equal_sums(perm):
            # print(f'YEP! {perm}')
            return True
    # print('nope.')
    return False


def perm_has_equal_sums(perm: tuple[int]) -> bool:
    middle_index: int = len(perm) // 2 + 1
    divider_index: int = middle_index
    initial_left_sum: int = sum(perm[:divider_index])
    initial_right_sum: int = sum(perm[divider_index:])

    # early exit: initial sums are equal
    if initial_left_sum == initial_right_sum:
        return True

    # initialize leftward crawl
    current_left_sum: int = sum(perm[:divider_index])
    current_right_sum: int = sum(perm[divider_index:])
    divider_index -= 1
    # move divider left from middle
    while divider_index >= 1:
        current_left_sum -= perm[divider_index]
        current_right_sum += perm[divider_index]
        print(f'\ndivider_index: {divider_index}\ncurrent_left_sum: {current_left_sum}\ncurrent_right_sum: {current_right_sum}')

        if current_left_sum == current_right_sum:
            return True

        divider_index -= 1
    # initialize rightward crawl
    current_left_sum = initial_left_sum
    current_right_sum = initial_right_sum
    divider_index = middle_index
    # move divider right from middle
    while divider_index < len(perm) - 1:
        current_left_sum += perm[divider_index]
        current_right_sum -= perm[divider_index]
        print(f'\ndivider_index: {divider_index}\ncurrent_left_sum: {current_left_sum}\ncurrent_right_sum: {current_right_sum}')

        if current_left_sum == current_right_sum:
            return True

        divider_index += 1
    return False


if __name__ == '__main__':
    # test_combo_1 = [15, 5, 10, 15, 10, 20, 35]
    # # should return True, since sum(15,5,10,15,10) == sum(20,35)
    # expected_result = True
    # actual_result = combo_has_equal_sums(test_combo_1)
    # print(f'expected: {expected_result}, actual: {actual_result}')
    # assert expected_result == actual_result
    #
    # test_combo_2 = [15, 5, 20, 10, 35]
    # # should return False, since no combination of subsets can have equal sums
    # expected_result = False
    # actual_result = combo_has_equal_sums(test_combo_2)
    # print(f'expected: {expected_result}, actual: {actual_result}')
    # assert expected_result == actual_result

    test_list_1 = [15, 5, 21, 15]
    # should return False, since no combination of subsets can have equal sums
    # NOTE: this will run long, as it will test all permutations
    expected_result = False
    actual_result = list_has_equal_sums(test_list_1)
    print(f'@@@ expected: {expected_result}, actual: {actual_result}')
    assert expected_result == actual_result

    test_list_2 = [15, 10, 20, 15, 10, 5, 35]
    # should return True, since sum(15,5,10,15,10) == sum(20,35)
    # but will have to use a combination
    expected_result = True
    actual_result = list_has_equal_sums(test_list_2)
    print(f'@@@ expected: {expected_result}, actual: {actual_result}')
    assert expected_result == actual_result

    # test_range = 5
    # test_list_3 = [random.randint(-test_range, test_range) for _ in range(test_range)]
    # print(f'test_list_3: {test_list_3}')
    # print(f'expected: ??, actual: {list_has_equal_sums(test_list_3)}')
