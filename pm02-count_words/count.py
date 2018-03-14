def count_words_0(s):
    sa = s.split()
    record = {}
    for i in sa:
        if i in record:
            record[i] += 1
        else:
            record[i] = 1
    return record

def count_words_1(s):
    sa = s.split()
    record = {}
    for i in sa:
        il = i.lower()
        if not i[0].isalnum():
            continue
        if il in record:
            record[il] += 1
        else:
            record[il] = 1
    return record

from collections import Counter
def count_words_2(s):
    return Counter(s.split())

def count_words_3(s):
    sn = []
    for i in s.split():
        sn.append(i.lower().strip(',;.!?"()-'))
    return Counter(sn)

import re
def count_words(s):
    return Counter(re.findall(r"[\w'-]+", s.lower()))


if __name__ == "__main__":
    s0 = "Oh what a day, oh what a lovely day!"
    res = count_words_1(s0)
    print(res)