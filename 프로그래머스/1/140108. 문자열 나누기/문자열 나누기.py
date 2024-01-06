def solution(s):
    answer = 0
    first = ''
    a = 0
    b = 0
    for i in s:
        if first == '':
            first = i
            a += 1
            continue
        
        if i == first:
            a += 1
        else:
            b += 1
        
        if a == b:
            first = ''
            a = 0
            b = 0
            answer += 1
    if first != '':
        answer += 1
    return answer