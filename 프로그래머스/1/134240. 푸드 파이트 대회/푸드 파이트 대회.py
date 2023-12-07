def solution(food):
    answer = ''
    for i in range(1,len(food)):
        fod = str(i)
        if food[i] > 1:
            answer += fod * (food[i]//2)
    return answer + '0' + answer[::-1]