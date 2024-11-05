# There's json core module and JSONObject related code
# see https://docs.python.org/3/library/json.html

import json

# creating a json object or file
# NOTE: remember to use double quotes
data_object_1: dict = {
    "key 1": 34,
    "key 2": ['a', 'b', 'c'],
    "key 3": {
        "key 1-1": "subthing",
        "key 1-2": "subthing 2",
    }
}
# same key-values, different order
# in parent and child objects
data_object_2: dict = {
    "key 2": ['a', 'b', 'c'],
    "key 1": 34,
    "key 3": {
        "key 1-2": "subthing 2",
        "key 1-1": "subthing",
    }
}
data_json_1 = json.dumps(data_object_1)
data_json_2 = json.dumps(data_object_2)
print(f'data_json_1 type: {type(data_json_1)}')
# NOTE: json.dumps deals with streams, so until the result is printed, written
#  to a file, or subject to some other operation that stops the stream, the
#  json.dumps process will keep running.
print(f'{data_json_1=}')
print(f'{data_json_2=}')

# comparison
## dictionaries are unordered
print(f'data_object_1 == data_object_2? {data_object_1 == data_object_2}') # True

## json objects are not (because they use streams or strings?)
print(f'data_json_1 == data_json_2? {data_json_1 == data_json_2}') # False
print(f'data_json_1 type: {type(data_json_1)}')

## so convert json objects to unordered data types
## NOTE: using json.loads will deserialize all objects in the json, BUT can only be used
##  on string, bytes, or bytesarray objects that are properly json formatted
data_json_1_dict = json.loads(data_json_1)
data_json_2_dict = json.loads(data_json_2)
print(f'data_json_1_dict == data_json_2_dict? {data_json_1_dict == data_json_2_dict}')
print(f'{data_json_1_dict=}')
print(f'data_json_1_dict type: {type(data_json_1_dict)}')
