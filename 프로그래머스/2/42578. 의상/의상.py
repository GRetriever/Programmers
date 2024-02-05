def solution(clothes):
    from collections import defaultdict
    answer = 1
    dict = defaultdict(list)
    for i in clothes:
        dict[i[1]].append(i[0])
    
    for i,j in dict.items():
        answer *= len(j)+1
        
    return answer-1