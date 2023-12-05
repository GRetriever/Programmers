def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        div = 0
        for j in range(1,int(i**0.5)+1):
            if i % j == 0:
                div += 2
        if i**0.5 % 1 == 0:
            div -= 1
        if div > limit:
            div = power
        answer += div
    return answer