def solution(nums):
    from itertools import combinations
    
    answer = 0
    for i in combinations(nums,3):
        s = 0
        for j in range(2,sum(i)):
            if sum(i) % j == 0:
                s += 1
        if s == 0:
            answer += 1             
    return answer

