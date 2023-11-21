def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        sort = sorted(array[i-1:j])
        answer.append(sort[k-1])
    return answer