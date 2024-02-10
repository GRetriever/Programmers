def solution(nums):
    from itertools import combinations
    answer = 0
    for i in combinations(nums,3):
        s = sum(i)
        div = 0
        for j in range(2,s):
            if s % j == 0:
                div += 1
                break
        if div == 0:
            answer += 1
    return answer
