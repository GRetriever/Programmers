def solution(k, m, score):
    answer = 0
    sor = sorted(score)[::-1]
    for i in range(0,len(score),m):
        if len(sor[i:i+m]) == m:
            answer += min(sor[i:i+m])*m
    return answer