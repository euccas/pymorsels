def lstrip0(iterable, obj):
    i = 0
    iterable_list = list(iterable)
    while i < len(iterable_list):
        if iterable_list[i] != obj:
            break
        i += 1

    for k in range(i, len(iterable_list)):
        yield iterable_list[k]

def lstrip(iterable, obj, key_func=None):
    if not key_func:
        key_func = lambda x: x == obj

    i = 0
    iterable_list = list(iterable)
    while i < len(iterable_list):
        if key_func(iterable_list[i]) is False:
            break
        i += 1

    for k in range(i, len(iterable_list)):
        yield iterable_list[k]


if __name__ == "__main__":
    lstrip0([1,1,1], 1)
    lstrip([1,1,1], 1)