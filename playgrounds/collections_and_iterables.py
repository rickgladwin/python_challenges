# List operations

test_list : list = [1,3,6,7,9,103]

print(f'{test_list=}')

print(f'{test_list[3:]=}')
print(f'{test_list[:3]=}')
print(f'{test_list[-2:]=}')

test_list.append(12)
test_list.remove(103)

print(f'{test_list=}')

test_list.extend([203, 305, 98, 23, 75])
print(f'{test_list=}')

# sort in place (no return)
test_list.sort()
print(f'after sort:         {test_list=}')

# reverse sort
test_list.sort(reverse=True)
print(f'after reverse sort: {test_list=}')

# tuple from list
test_tuple : tuple = tuple(test_list)
print(f'                   {test_tuple=}')

# tuple from destructuring
(age, income) = "32,120000".split(',')
print(f'{(age)=}')
# NOTE: parentheses are redundant here
print(f'{income=}')
