# ./src/max_negative_repr.py

def max_negative_repr(numbers: list[int]) -> int:
    """
    Find the largest positive number that has its negative representation
    also present in the list.

    The function runs in O(N) time. It converts the list into a set for
    fast membership lookups. Then it iterates over positive numbers and
    checks whether the corresponding negative exists.

    Args:
        numbers (List[int]): List of integers to analyze.

    Returns:
        int: The maximal positive number whose negative counterpart exists,
             or -1 if no such number is found.

    Examples:
        >>> max_negative_repr([100, 4, 1, -1, -4, -100])
        100
        >>> max_negative_repr([100, 4, 1, 1, 4, 100, -1])
        1
        >>> max_negative_repr([100, 4, 1, 1, 4, 100, 1, -2])
        -1
    """
    s = set(numbers)
    res = -1

    for num in numbers:
        if num > 0 and -num in s:
            res = max(res, num)

    return res
