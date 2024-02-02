def solution(numbers):
    from itertools import combinations
    answer = []
    for i,j in combinations(numbers,2):
        answer.append(i+j)
    return sorted(set(answer))