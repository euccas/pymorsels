def compact(seq):
    if seq is None or len(seq) == 0:
        return []
    cseq = [seq[0]]
    for i in range(1, len(seq)):
        if seq[i] != seq[i-1]:
            cseq.append(seq[i])
    return cseq

