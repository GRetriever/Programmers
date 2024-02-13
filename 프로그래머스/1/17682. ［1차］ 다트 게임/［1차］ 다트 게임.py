def solution(dartResult):
    answer = []
    dict = {'S':1,'D':2,'T':3}
    score = ''
    for i in dartResult:
        if i.isdigit():
            score += i
        elif i in dict:
            answer.append(int(score)**dict[i])
            score = ''
        elif i == '*':
            answer[-1] *= 2
            if len(answer) > 1:
                answer[-2] *= 2
        elif i == '#':
            answer[-1] *= -1
    return sum(answer)