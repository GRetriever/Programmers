def solution(survey, choices):
    from collections import defaultdict
    answer = ''
    score = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    dict = defaultdict(int)
    char = ['RT','CF','JM','AN']
    
    for i,j in zip(survey,choices):
        if j < 4:
            dict[i[0]] += score[j]
        if j > 4:
            dict[i[1]] += score[j]
    
    for i,j in char:
        if dict[i] >= dict[j]:
            answer += i
        else:
            answer += j
            
    return answer