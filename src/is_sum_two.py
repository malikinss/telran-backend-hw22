# ./src/is_sum_two.py

def is_sum_two(numbers: list[int], sum: int) -> bool:
    """
    Check if a list contains two numbers whose sum equals the given target.

    This function runs in O(N) time using a hash set to track previously
    seen numbers. For each number `x` in the list, it checks whether
    `sum_ - x` has already been seen. If yes, a valid pair exists.

    Args:
        numbers (list[int]): List of integers to search within.
        sum_ (int): Target sum to check for.

    Returns:
        bool: True if there exist two numbers whose sum equals `sum_`,
              otherwise False.

    Examples:
        >>> is_sum_two([1, 2, 3, 4], 4)
        True
        >>> is_sum_two([1, 2, 3, 4], 2)
        False
    """
    seen: set[int] = set()
    for num in numbers:
        if (sum - num) in seen:
            return True
        seen.add(num)
    return False
