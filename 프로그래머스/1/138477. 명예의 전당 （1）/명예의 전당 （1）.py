def solution(k, score):
    answer = []
    honour = []
    for i in score:
        honour.append(i)
        honour.sort(reverse=True)
        
        if len(honour) > k:
            honour.pop()
        
        answer.append(honour[-1])
        
    return answer