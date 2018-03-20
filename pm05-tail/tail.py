def tail(nums, n):
    if nums is None or len(nums) == 0 or n < 0:
        return []

    if len(nums) >= n:
        return list(nums[len(nums)-n:])
    return list(nums)

def tail_1(sequence, n):
    """Return the last n items of given sequence."""
    if n == 0:
        return []
    return list(sequence[-n:])

def tail_2(iterable, n):
    """Return the last n items of given iterable."""
    sequence = list(iterable)
    if n <= 0:
        return []
    return sequence[-n:]

