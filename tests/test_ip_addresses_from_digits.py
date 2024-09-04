from ip_addresses_from_digits import generate_ip_addresses_from_digits, list_to_ip_address, \
    multiple_lists_to_ip_addresses


class TestIpAddressesFromDigitsSuccess:
    def test_generates_empty_output_from_empty_input(self):
        test_input = ''
        expected_output = []
        result = generate_ip_addresses_from_digits(test_input)
        assert result == expected_output

    def test_generates_empty_output_from_too_short_input(self):
        test_input = '123'
        expected_output = []
        result = generate_ip_addresses_from_digits(test_input)
        assert result == expected_output

    def test_generates_output_from_minimal_input(self):
        test_input = '1234'
        expected_output = ['1.2.3.4']
        result = generate_ip_addresses_from_digits(test_input)
        assert result == expected_output

    def test_generates_output_from_input_length_5(self):
        test_input = '12434'
        expected_output = ['1.2.4.34', '1.2.43.4', '1.24.3.4', '12.4.3.4']
        result = generate_ip_addresses_from_digits(test_input)
        assert result == expected_output

    def test_converts_single_digit_segments_to_ip_address(self):
        test_input = ['1', '2', '3', '4']
        expected_output = '1.2.3.4'
        result = list_to_ip_address(test_input)
        assert result == expected_output

    def test_converts_multi_digit_segments_to_ip_address(self):
        test_input = ['123', '22', '30', '255']
        expected_output = '123.22.30.255'
        result = list_to_ip_address(test_input)
        assert result == expected_output

    def test_converts_list_of_segment_lists_to_list_of_ip_addresses(self):
        test_input = [['1', '2', '3', '4'], ['34', '255', '1', '0']]
        expected_output = ['1.2.3.4', '34.255.1.0']
        result = multiple_lists_to_ip_addresses(test_input)
        assert result == expected_output


class TestIpAddressesFromDigitsFailure:
    def test_invalidates_input_containing_characters(self):
        test_input = '123A345'
        try:
            generate_ip_addresses_from_digits(test_input)
        except Exception:
            assert True
        else:
            assert False

    def test_invalidates_address_segment_count_other_than_4(self):
        test_input = ['1', '2', '3']
        try:
            list_to_ip_address(test_input)
        except Exception:
            assert True
        else:
            assert False

