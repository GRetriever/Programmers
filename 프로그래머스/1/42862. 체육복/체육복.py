def solution(n, lost, reserve):
    s = set(lost) & set(reserve)
    l = sorted(list(set(lost) - set(s)))
    r = sorted(list(set(reserve) - set(s)))
            
    for i in l:
        if i-1 in r:
            r.remove(i-1)
        elif i+1 in r:
            r.remove(i+1)
        else:
            n -= 1
    return n