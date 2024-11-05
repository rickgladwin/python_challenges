# tuple
# n-dimensional collection
# ordered
# immutable
# iterable
# mixed-type elements
from typing import Iterator, AnyStr

# basics
test_tuple: tuple = (2, 'something', ['a', 'b', 'c'])
print(f'{test_tuple[0]}')
for element in test_tuple:
    print(f'{element}')

# test_tuple[1] = 'something else' # TypeError

# nested iteration
## e.g. os.walk(path) -> Iterator[tuple[AnyStr, list[AnyStr], list[AnyStr]]]
## os.walk builds an iterator from a tree of folders and files
iterable_list = [
    ('parent 1', ['child 1-1', 'child 1-2'], ['subchild 1-1', 'subchild 1-2']),
    ('parent 2', ['child 2-1'], ['subchild 2-1', 'subchild 2-2']),
    ('parent 3', ['child 3-1', 'child 3-2', 'child 3-3'], []),
]

tuple_iterator: Iterator[tuple[AnyStr, list[AnyStr], list[AnyStr]]] = iter(iterable_list)
# shows only paths that have subchildren
for parent, children, subchildren in tuple_iterator:
    for child in children:
        for subchild in subchildren:
            print(f'parent: {parent}, child: {child}, subchild: {subchild}')
print('----')
print(f'{str(tuple_iterator)}')
# builds display path while traversing the nested iterables
# NOTE: iterator must be rebuilt before iterating on it again.
#  Performing the iteration consumes the iterator.
tuple_iterator = iter(iterable_list)
for parent, children, subchildren in tuple_iterator:
    print(f'- {parent=}')
    path_string: str = parent
    for child in children:
        # print(f'{child=}')
        path_string = parent + '/' + child
        print(f'-- {path_string}')
        for subchild in subchildren:
            # print(f'{subchild=}')
            path_string = parent + '/' + child + '/' + subchild
            print(f'--- {path_string=}')
