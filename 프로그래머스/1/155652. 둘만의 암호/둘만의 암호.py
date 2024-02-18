def solution(s, skip, index):
    answer = ''
    alp = sorted(set('abcdefghijklmnopqrstuvwxyz') - set(skip))
    for i in s:
        alp_index = alp.index(i) + index
        answer += alp[alp_index % len(alp)]
    
    return answer