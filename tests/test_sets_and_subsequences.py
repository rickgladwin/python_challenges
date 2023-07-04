from sets_and_subsequences import subsequences


class TestSubsequences:
    def test_finds_subsequences_of_sequence_with_length_1(self):
        test_sequence = ['a']
        expected_result = [['a']]
        result = subsequences(test_sequence)
        assert result == expected_result

    def test_finds_subsequences_of_sequence_with_length_2(self):
        test_sequence = ['a', 'b']
        expected_result = [['a'], ['b'], ['a', 'b']]
        result = subsequences(test_sequence)
        assert result == expected_result

    def test_finds_subsequences_of_sequence_with_length_3(self):
        test_sequence = ['a', 'b', 'c']
        expected_result = [['a'], ['b'], ['c'], ['a', 'b'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
        result = subsequences(test_sequence)
        assert result == expected_result

