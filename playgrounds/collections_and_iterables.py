# List operations

test_list : list = [1,3,6,7,9, 103]

print(f'{test_list[3:]=}')
print(f'{test_list[:3]=}')

test_list.append(12)
test_list.remove(103)

print(f'{test_list=}')

# tuple from list

test_tuple : tuple = tuple(test_list)

print(f'{test_tuple=}')
