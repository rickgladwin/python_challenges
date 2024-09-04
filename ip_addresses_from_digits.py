# Given a string of digits, generate all possible valid IP address combinations.
#
# IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255.
# Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.
#
# For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123']


# strategy:
# recursive function to build and record "x valid segments from here" where x is the "here + 1" segment
# optimizations:
# - the possible combinations of digits in the address segments will depend on the
#   total length of the input string. Calculate these segment lengths in advance,
#   and only look to fill those segments. For example, '1234' is valid, but don't let
#   the function use '123' as a first segment.

def generate_ip_addresses_from_digits(digits: str) -> list:
    result: list = []
    # guard minimum digit count
    if len(digits) < 4:
        print(f'input length too short ({len(digits)}')
        return result
    # guard non-integer input
    try:
        int_digits = int(digits)
    except ValueError:
        raise Exception('input must be a string of digits only')

    digits_iter = [x for x in digits]

    # recursive function
    def append_segments(remaining_digits: list[str] = digits_iter, current_segments: list[str] = [],
                        remaining_depth: int = 4):
        nonlocal result
        # print(f'{remaining_digits=}')
        if remaining_depth == 0 and len(current_segments) == 4:
            print(f'-- new IP address: {current_segments}')
            result.append(current_segments)
            return None

        # to the current segments, append the next 1, 2, and 3 digits
        for i in range(1, 4):
            if len(remaining_digits) >= i:
                print(f'{remaining_digits=}')
                print(f'{i=}')
                cloned_segments = current_segments.copy()
                # TODO: exit for loop if first digit in segment is 0 AND segment length is > 1
                # split the remaining digits after i
                pre_pre_chunk = remaining_digits[:i]
                print(f'{pre_pre_chunk=}')
                pre_chunk = ''.join(remaining_digits[:i])
                print(f'{pre_chunk=}')
                post_chunk = remaining_digits[i:]
                print(f'{post_chunk=}')
                # append the chunk before the split to the current segments
                print(f'appending pre_chunk: {pre_chunk}')
                cloned_segments.append(pre_chunk)
                # run the recursive function with the chunk after the split
                append_segments(post_chunk, cloned_segments, remaining_depth - 1)
            return None

    # initial recursive call
    append_segments()

    # format result
    result = multiple_lists_to_ip_addresses(result)

    return result


def list_to_ip_address(segments: list) -> str:
    ip_address = ''
    # validate length
    if len(segments) != 4:
        raise Exception('input parameter must have length 4')

    for i in range(0, 4):
        print(f'{i=}')
        ip_address = ip_address + segments[i] + '.'
    ip_address = ip_address[:-1]

    return ip_address


def multiple_lists_to_ip_addresses(segments_list: list[list]) -> list[str]:
    ip_addresses = []
    for segments in segments_list:
        print(f'{segments=}')
        ip_addresses.append(list_to_ip_address(segments))

    return ip_addresses


if __name__ == "__main__":
    test_digits = "1234"
    expected_result = ['1.2.3.4']

    test_result = generate_ip_addresses_from_digits(test_digits)
    print(f'{test_result=}')
    assert (test_result == expected_result)
