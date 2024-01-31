def solution(food):
    answer = ''
    for i,num in enumerate(food):
        if i == 0:
            continue
        answer += str(i)*(num//2)
    return answer +'0' + answer[::-1]