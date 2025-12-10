# ./tests/test_is_sum_two.py
import unittest

from src import is_sum_two


class TestIsSumTwo(unittest.TestCase):
    """
    Unit tests for the `is_sum_two` function.
    """

    def test_cases(self):
        """
        Test multiple scenarios for `is_sum_two`.

        This includes:
            - Basic cases
            - Edge cases (single element, zeros)
            - Large numbers
            - Duplicates
            - Negative numbers
        """
        test_data = [
            # Basic cases
            ([10, 15, 3, 7], 17, True),
            ([1, 2, 3, 4], 8, False),
            ([-1, 0, 1, 2], 1, True),
            ([], 5, False),
            ([5], 10, False),

            # Edge cases
            ([1], 2, False),
            ([0, 0], 0, True),
            ([1, 2, 3], -1, False),
            ([1000000, -1000000], 0, True),

            # Large numbers
            ([10**9, -10**9], 0, True),
            ([10**9, 10**9], 1, False),
            ([2**31 - 1, -2**31 + 1], 0, True),
            ([2**31, 2**31], 2**32, True),
            ([-2**31, 2**31 - 1], -1, True),

            # Duplicates
            ([5, 5, 5], 10, True),
            ([1, 1, 1], 3, False),
            ([2, 2, 2, 2], 4, True),
            ([3, 3, 3], 7, False),
            ([0, 0, 0], 0, True),

            # Negative numbers
            ([-5, -3, -2, -1], -4, True),
            ([-1, -2, -3], -7, False),
            ([-10, 5, 15], 5, True),
            ([-10, -20, -30], -25, False),
            ([-1, 1, 0], 0, True),
            ([-100, -200, -300], -50, False),
        ]

        for numbers, target, expected in test_data:
            with self.subTest(numbers=numbers, target=target):
                self.assertEqual(is_sum_two(numbers, target), expected)


if __name__ == "__main__":
    unittest.main()
