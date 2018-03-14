def negate_0(numlist):
    # this is slower than negate_1, ~ 2* time
    if numlist is None or len(numlist) == 0:
        return []

    # method: multiple -1
    # O(N)
    for k in range(len(numlist)):
        for i in range(len(numlist[k])):
            numlist[k][i] *= -1

    return numlist

def negate_1(numlist):
    # don't use n * -1, just use -n, it's faster
    if numlist is None or len(numlist) == 0:
        return []

    return [
        [-n for n in sublist]
        for sublist in numlist
        ]

def negate(numlist):
    return negate_1(numlist)


if __name__ == "__main__":
    import datetime

    numlist = [[1,2,3],[-1,2,-3],[1000,200,-2]]

    before_exec = datetime.datetime.now()
    print(before_exec.strftime("%H:%M:%S.%f"))

    for i in range(10000):
        negate_1(numlist)

    after_exec = datetime.datetime.now()
    print(after_exec.strftime("%H:%M:%S.%f"))

    time_diff = after_exec - before_exec
    print(time_diff)