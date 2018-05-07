def uniques_only_0(iterable):
    """
    The problem is set doesn't ensure order
    """
    return set(iterable)

def uniques_only_1(iterable):
    """
    This works but it's going to be very slow for large lists of items because checking for containment (X not in Y) in a list requires looping through the whole list.
    """
    items = []
    for n in iterable:
        if n not in items:
            items.append(n)

    return items

def uniques_only(iterable):
    """
    This works only for sequence, but not for all iterable
    """
    items = []
    for i, n in enumerate(iterable):
        if n not in iterable[:i]:
            items.append(n)

    return items