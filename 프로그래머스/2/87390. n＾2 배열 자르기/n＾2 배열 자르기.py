def solution(n, left, right):
    answer = []
    
    for i in range(left,right+1):
        r = i // n
        c = i % n
        
        num = max(r,c) + 1
        answer.append(num)
    
    return answer