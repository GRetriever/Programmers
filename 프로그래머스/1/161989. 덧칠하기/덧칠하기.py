def solution(n, m, section):
    answer = 1
    current = section[0]
    for i in section:
        if current + m -1 < i:
            current = i
            answer += 1
    return answer