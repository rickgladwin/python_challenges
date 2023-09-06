from ip_addresses_from_digits import generate_ip_addresses_from_digits


class SuccessCases:
    def test_generates_empty_output_from_empty_input(self):
        test_input = ''
        expected_output = []
        result = generate_ip_addresses_from_digits(test_input)
        assert result == expected_output
