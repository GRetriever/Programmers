def solution(number, limit, power):
    answer = []
    
    for i in range(1,number+1):
        num = 0
        for j in range(1,int(i**0.5) + 1):
            if i % j == 0:
                num += 1
                if j*j != i:
                    num += 1
        if num > limit:
            answer.append(power)
        else:
            answer.append(num)
    return sum(answer)