def solution(d, budget):
    a = sorted(d)
    answer = 0
    sum = 0
    for i in a:
        if sum + i <= budget:
            sum += i
            answer += 1
    return answer