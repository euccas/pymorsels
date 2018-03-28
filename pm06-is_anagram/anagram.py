def is_anagram_0(s1, s2):
    """
    This is my first solution, and it's incorrect because this method checks palindrome, not anagram.
    """
    if s1 is None or s2 is None:
        return False

    if len(s1) != len(s2):
        return False

    s1_list = list(s1)
    s2_list = list(s2)
    for i in range((len(s1_list))):
        #print("{0}, {1}".format(s1_list[i], s2_list[-i]))
        if s1_list[i] != s2_list[len(s2_list)-1-i]:
            return False

    return True

def is_anagram_1(s1, s2):
    from collections import Counter
    if s1 is None or s2 is None:
        return False

    # make sure your function works with mixed case
    if Counter([c.lower() for c in list(s1)]) == Counter([c.lower() for c in list(s2)]):
        return True

    return False

def is_anagram(s1, s2):
    if s1 is None or s2 is None:
        return False

    from _collections import defaultdict
    rec1 = defaultdict(int)
    for c in s1:
        rec1[c.lower()] += 1

    rec2 = defaultdict(int)
    for c in s2:
        rec2[c.lower()] += 1

    if rec1 == rec2:
        return True

    return False

if __name__ == "__main__":
    res = is_anagram_0("tea", "aet")
    expected_res = True
    print("res = {0}".format(res))
    assert(res == expected_res)


