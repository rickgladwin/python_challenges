# Write a function to flatten a nested dictionary. Namespace the keys with a period.
#
# For example, given the following dictionary:
#
# {
#     "key": 3,
#     "foo": {
#         "a": 5,
#         "bar": {
#             "baz": 8
#         }
#     }
# }
# it should become:
#
# {
#     "key": 3,
#     "foo.a": 5,
#     "foo.bar.baz": 8
# }
# You can assume keys do not contain dots in them, i.e. no clobbering will occur.

# solution 1:
# multi-threading:
# a thread records its own sub_result, adds that result to the result when it hits a non-dict value
# one thread per key in a dict
# threads do work then return null


def flatten(source: dict) -> dict:
    flattened = {}

    def build_key_val(source_dict: dict, built_key: str = ''):
        for key, val in source_dict.items():
            sub_key = f'{built_key}.{key}'
            if type(val) is not dict:
                flattened[sub_key.lstrip('.')] = val
                continue
            else:
                build_key_val(val, sub_key)
        return None

    build_key_val(source)

    return flattened
