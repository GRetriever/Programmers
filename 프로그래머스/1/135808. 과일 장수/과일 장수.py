def solution(k, m, score):
    answer = 0
    score = sorted(score,reverse=True)
    for num in score[m-1::m]:
        answer += num*m
    return answer