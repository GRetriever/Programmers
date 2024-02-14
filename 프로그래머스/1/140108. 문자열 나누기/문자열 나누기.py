def solution(s):
    answer = 0
    x = 0
    y = 0
    first = ''
    for i in s:
        if first == '':
            first = i
            x += 1
            continue
        if i == first:
            x += 1
        else:
            y += 1
        if x == y:
            answer += 1
            x,y = 0,0
            first = ''
    if x != y:
        answer += 1
    return answer