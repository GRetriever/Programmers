def solution(citations):
    c = sorted(citations,reverse=True)
    for i in range(len(c)):
        if c[i] < i+1:
            return i
    return len(c)
        