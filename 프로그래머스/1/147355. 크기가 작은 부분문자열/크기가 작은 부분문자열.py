def solution(t, p):
    answer = 0
    l = len(p)
    for i in range(len(t)):
        if len(t[i:l+i]) != l:
            break
        elif t[i:l+i] <= p:
            answer += 1
    return answer