def solution(answers):
    answer = [0,0,0]
    result = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
            if a[i%len(a)] == answers[i]:
                answer[0] += 1
            if b[i%len(b)] == answers[i]:
                answer[1] += 1
            if c[i%len(c)] == answers[i]:
                answer[2] += 1
    for i,score in enumerate(answer):
        if max(answer) == score:
            result.append(i+1)
    return result