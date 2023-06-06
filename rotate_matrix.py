# Given an N by N matrix, rotate it by 90 degrees clockwise.
#
# For example, given the following matrix:
#
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# you should return:
#
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
# Follow-up: What if you couldn't use any extra space?

import numpy as np


# What are we doing when we rotate a matrix? We're taking each position's x and y distance from the center of the
#  matrix, a vector in essence, and rotating that vector.
# For a 90-degree rotation, this is equivalent to swapping the x and y distances, and then negating the new y distance.
# So, to get a new matrix, for each position in the starting matrix:
#  - Calculate the x and y distances from the center of the matrix
#  - Swap the x and y distances
#  - Negate the new y distance
#  - Add the new x and y distances to the center of the matrix to get the new position

def rotate_90(matrix: list[list]) -> list[list]:
    """Rotate a matrix 90 degrees clockwise
    :param matrix: N x N matrix to rotate
    :returns: rotated matrix"""

    # A rotation by 90 degrees is equivalent to a transpose followed by a reflection in the y-axis at the
    #  midpoint of the matrix
    #  So first swap the x and y indices (not the indices relative to the midpoint)
    #  Then reflect the y indices relative to the midpoint (i.e. reverse each row)

    # [[1, 2, 3],
    #  [4, 5, 6],
    #  [7, 8, 9]]
    # you should return:
    #
    # [[7, 4, 1],
    #  [8, 5, 2],
    #  [9, 6, 3]]

    # use numpy
    new_matrix = np.array(matrix)
    # transpose the matrix
    new_matrix = np.transpose(new_matrix)
    print(f'transposed: {new_matrix}')
    # reverse the rows
    for index, row in enumerate(new_matrix):
        # new_matrix[index] = np.ndarray.tolist(np.flip(row))
        new_matrix[index] = np.flip(row)
    print(f'reversed: {new_matrix}')
    # convert back to list

    return new_matrix.tolist()


if __name__ == '__main__':
    test_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    expected_result = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]

    print('\noriginal matrix:')
    print(test_matrix)

    print('\nexpected result:')
    print(expected_result)

    result = rotate_90(test_matrix)
    print('\nrotated matrix:')
    print(result)
    print(f'type of result: {type(result)}')
    print(f'type of result[0]: {type(result[0])}')

    assert(result == expected_result)
