import math
import unittest
import unbiased_flip_from_biased_flip as ufbf

class UnbiasedFlipFromBiasedFlip(unittest.TestCase):
    def test_biased_tosses_match_bias(self):
        # counts from biased flips should match bias
        expected_toss_bias = 0.75  # NOTE: must match function
        heads_count = 0
        tails_count = 0
        test_toss_count = 100
        for _ in range(0, test_toss_count):
            if ufbf.toss_biased() == 'heads':
                # print(f'--heads')
                heads_count += 1
            else:
                # print(f'--tails')
                tails_count += 1

        tolerance = math.sqrt(test_toss_count) / 100
        print()
        print(f'#{heads_count=}')
        print(f'#{tails_count=}')

        result_ratio = heads_count / test_toss_count
        print(f'#{result_ratio=}')
        print(f'#{tolerance=}')
        result_difference = result_ratio - expected_toss_bias
        print(f'#{result_difference=}')

        assert abs(heads_count / test_toss_count - expected_toss_bias) <= tolerance

        # self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
