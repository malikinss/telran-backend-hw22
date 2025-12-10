# tests/test_max_negative_repr.py
import unittest

from src import max_negative_repr


class TestMaxNegativeRepr(unittest.TestCase):
    """
    Unit tests for the `max_negative_repr` function.
    """

    def test_cases(self):
        """
        Test multiple scenarios for `max_negative_repr`.

        This includes:
            - Basic cases with positive numbers having negative counterparts
            - Cases where no positive number has a negative counterpart
            - Duplicates
            - Mixed numbers
            - Large numbers
        """
        test_data = [
            # Basic cases
            ([100, 4, 1, -1, -4, -100], 100),
            ([1, 4, 100, -1, -4], 4),
            ([5, -5], 5),
            ([10, 20, -10], 10),

            # No positive number with negative counterpart
            ([-1, -2, -3], -1),
            ([1, 2, 3], -1),
            ([0], -1),
            ([], -1),

            # Duplicates
            ([1, 1, -1, -1], 1),
            ([2, 2, -2, 2], 2),
            ([5, 5, -5, 5, -5], 5),

            # Mixed numbers
            ([1, 2, -1, 3, -3], 3),
            ([10, -5, -10, 5], 10),
            ([50, -100, 100, -50], 100),

            # Large numbers
            ([10**9, -10**9], 10**9),
            ([2**31, -2**31], 2**31),
            ([2**31 - 1, -(2**31 - 1)], 2**31 - 1),
        ]

        for numbers, expected in test_data:
            with self.subTest(numbers=numbers):
                self.assertEqual(max_negative_repr(numbers), expected)


if __name__ == "__main__":
    unittest.main()
