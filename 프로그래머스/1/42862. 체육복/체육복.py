def solution(n, lost, reserve):
    answer = n-len(lost)
    s = set(lost) & set(reserve)
    answer += len(s)
    l = sorted(list(set(lost) - set(s)))
    r = sorted(list(set(reserve) - set(s)))
            
    for i in l:
        if i-1 in r:
            r.remove(i-1)
            answer += 1
        elif i+1 in r:
            r.remove(i+1)
            answer += 1
    return answer