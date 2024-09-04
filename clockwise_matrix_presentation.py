# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
#
# For example, given the following matrix:
#
# [[1,  2,  3,  4,  5],
#  [6,  7,  8,  9,  10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20]]
# You should print out the following:
#
# 1
# 2
# 3
# 4
# 5
# 10
# 15
# 20
# 19
# 18
# 17
# 16
# 11
# 6
# 7
# 8
# 9
# 14
# 13
# 12

def print_spiral(input_matrix: list[list]) -> list:
    matrix_width = len(input_matrix[0])
    matrix_height = len(input_matrix)
    result = []

    # left to right
    # top to bottom
    # right to left
    # bottom to top

    right_start = 0
    right_limit = matrix_width - 1
    down_start = 0
    down_limit = matrix_height - 1
    left_start = matrix_width - 1
    left_limit = 0
    up_start = matrix_height - 1
    up_limit = 0 - 1

    for i in range(right_start, right_limit + 1):
        result.append(input_matrix[down_start][i])
    for i in range(down_start, down_limit + 1):
        result.append(input_matrix[i][right_limit])
    for i in range(left_start, left_limit, -1):
        result.append(input_matrix[down_limit][i])
    for i in range(up_start, up_limit, -1):
        result.append(input_matrix[i][left_limit])



