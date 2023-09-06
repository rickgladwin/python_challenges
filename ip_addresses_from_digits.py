# Given a string of digits, generate all possible valid IP address combinations.
#
# IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255.
# Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.
#
# For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123']
import re


# strategy:
# recursive function to build and record "x valid segments from here" where x is the "here + 1" segment

def generate_ip_addresses_from_digits(digits: str) -> list:
    result: list = []
    #guard minimal digits
    if len(digits) < 4:
        return result
    # guard "numbery" string
    regex_match = re.match()
    # TODO: validate only strings that can be converted to integers directly using int()
    #  That is, no non-digit characters, ignore starting zeroes

    return result


if __name__ == "__main__":
    test_digits = "1234"
    expected_result = ['1.2.3.4']

    test_result = ip_addresses(test_digits)
    print(f'{test_result=}')
    assert(test_result == expected_result)
