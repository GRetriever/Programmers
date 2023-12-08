def solution(participant, completion):
    from collections import Counter
    p = Counter(participant)
    c = Counter(completion)
    m = p-c
    return ''.join(list(m.keys()))
