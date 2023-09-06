from ip_addresses_from_digits import generate_ip_addresses_from_digits


class TestIpAddressesFromDigits:
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

