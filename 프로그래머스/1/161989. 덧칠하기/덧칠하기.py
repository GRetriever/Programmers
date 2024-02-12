def solution(n, m, section):
    answer = 1
    cur = section[0]
    for i in section:
        if cur + m - 1 < i:
            cur = i
            answer += 1
    return answer