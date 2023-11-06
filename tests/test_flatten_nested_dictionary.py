import unittest
import flatten_nested_dictionary as fnd


class FlattenNestedDictionary(unittest.TestCase):

    def test_flattens_2_level_dictionary(self):
        test_dict = {
            "key": 3,
            "foo": {
                "a": 5,
                "bar": {
                    "baz": 8
                }
            }
        }

        expected_output = {
            "key": 3,
            "foo.a": 5,
            "foo.bar.baz": 8
        }

        result = fnd.flatten(test_dict)

        self.assertEqual(expected_output, result)

    def test_flattens_depth_1_dictionary(self):
        test_dict = {
            'key_1': 3,
            'key_2': 'ok',
            'key_3': 5,
        }

        expected_output = test_dict

        result = fnd.flatten(test_dict)

        self.assertEqual(expected_output, result)

    def test_flattens_minimal_dictionary(self):
        test_dict = {
            "test_key": 5,
        }

        expected_result = {
            "test_key": 5,
        }

        result = fnd.flatten(test_dict)

        self.assertEqual(expected_result, result)

    def test_flattens_depth_2_dictionary(self):
        test_dict = {
            'key_1': {
                'key_1_1': 5,
            }
        }

        expected_output = {
            'key_1.key_1_1': 5,
        }

        result = fnd.flatten(test_dict)

        self.assertEqual(expected_output, result)


if __name__ == '__main__':
    unittest.main()
