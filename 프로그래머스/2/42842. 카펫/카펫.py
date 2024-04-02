def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1,total):
        j = total // i
        if i >= j and j*i == total and (i-2)*(j-2) == yellow:
            answer.append(i)
            answer.append(j)
            break
    return answer