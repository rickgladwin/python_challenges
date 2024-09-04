# given a list of numbers, find a combination of those numbers that
# sums to a target number
import itertools

# numbers = [1, 2, 3, 7, 7, 9, 10]
# numbers = [177.03, 93.04, 134.45, 157.53, 583.21, 116.36, 622.78, 670.38, 2694.69, 218.00]
# this list (with two errors where the thousands separators are) works with combination
# (656.8, 198.48, 157.53, 115.21, 583.21, 2, 891.7, 152.21, 116.36, 622.78, 2, 424.93, 374.42, 275.84)
#
# numbers = [
#     656.80,
#     19.43,
#     177.03,
#     198.48,
#     93.04,
#     134.45,
#     157.53,
#     115.21,
#     583.21,
#     2,891.70,
#     152.21,
#     116.36,
#     622.78,
#     670.38,
#     2,694.69,
#     424.93,
#     374.42,
#     275.84,
#     218.00,
# ]
# this list works in these combinations:
# (19.43, 198.48, 93.04,   583.21, 116.36,   2694.69, 374.42, 275.84, 218.0)
# (134.45, 157.53, 115.21, 583.21, 670.38,   2694.69,                 218.0)
numbers = [
    656.80,
    19.43,
    177.03,
    198.48,
    93.04,
    134.45,
    157.53,
    115.21,
    583.21,
    2891.70,
    152.21,
    116.36,
    622.78,
    670.38,
    2694.69,
    424.93,
    374.42,
    275.84,
    218.00,
]
# target = 10
# Research and Training total
target = 4573.47

result = [seq for i in range(len(numbers), 0, -1)
          for seq in itertools.combinations(numbers, i)
          if sum(seq) == target]

print(result)
