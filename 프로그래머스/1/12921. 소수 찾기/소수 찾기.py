def solution(n):
    # answer = 0
    # for i in range(2,n+1):
    #     prime = 0
    #     for j in range(2,i):
    #         if i % j == 0:
    #             prime += 1
    #             break
    #     if prime == 0:
    #         answer += 1
    # return answer
    num = set(range(2,n+1))
    
    for i in range(2,n+1):
        if i in num:
            num -= set(range(2*i,n+1,i))
    return len(num)
