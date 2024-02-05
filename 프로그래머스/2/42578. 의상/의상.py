def solution(clothes):
    from collections import defaultdict
    answer = 1
    dict = defaultdict(list)
    for i in clothes:
        dict[i[1]].append(i[0])
    
    for i,j in dict.items():
        answer *= len(j)+1
        
    return answer-1

# 모자 : 2가지 - 총 3가지 경우의 수
# 안경 : 1가지 - 총 2가지 경우의 수
# 근데 하나는 입어야 되니 아무 것도 안입는 경우의 수 -1