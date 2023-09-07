from ip_addresses_from_digits import generate_ip_addresses_from_digits


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


class TestIpAddressesFromDigitsFailure:
    def test_invalidates_input_containing_characters(self):
        test_input = '123A345'
        try:
            generate_ip_addresses_from_digits(test_input)
        except Exception:
            assert True
        else:
            assert False

