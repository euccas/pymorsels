def group_by(nums, key_func=None):
    group_result = {}

    if not key_func:
        for n in nums:
            if n in group_result:
                group_result[n].append(n)
            else:
                group_result[n] = [n]
        return group_result


    for n in nums:
        i = key_func(n)
        if i in group_result:
            group_result[i].append(n)
        else:
            group_result[i] = [n]

    return group_result