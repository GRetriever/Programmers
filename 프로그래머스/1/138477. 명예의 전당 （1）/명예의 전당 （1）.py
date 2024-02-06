def solution(k, score):
    honour = []
    answer = []
    for num in score:
        if len(honour) != k:
            honour.append(num)
            answer.append(min(honour))
            honour.sort()
        else:
            honour[0] = max(honour[0],num)
            answer.append(min(honour))
            honour.sort()
    return answer