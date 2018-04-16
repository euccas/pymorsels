def multimax(iterable):
    if iterable is None:
        return []

    maxvars = []
    max = iterable[0]
    for item in iterable:
        if item > max:
            max = item

    for item in iterable:
        if item == max:
            maxvars.append(item)

    return maxvars

def multimax1(iterable):
    if iterable is None:
        return []

    from collections import Counter
    record = Counter(iterable)
