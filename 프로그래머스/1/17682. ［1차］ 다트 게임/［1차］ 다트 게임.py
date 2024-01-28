def solution(dartResult):
    answer = []
    score = ''
    dict = {'S':1,'D':2,'T':3}
    for i in dartResult:
        if i.isdigit():
            score += i
        elif i in dict:
            answer.append(int(score)**dict[i])
            score = ''
        elif i == '*':
            answer[-1] *= 2
            if len(answer) >= 2:
                answer[-2] *= 2
        elif i == '#':
            answer[-1] *= -1
    return sum(answer)