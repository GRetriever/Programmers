def solution(s, skip, index):
    answer = ''
    alp = sorted(set('abcdefghijklmnopqrstuvwxyz') - set(skip))
    for i in s:
        answer += alp[(alp.index(i)+index)%len(alp)]
    return answer