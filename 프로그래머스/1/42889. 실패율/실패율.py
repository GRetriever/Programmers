def solution(N, stages):
    dict = {}
    l = len(stages)
    for i in range(1,N+1):
        if stages.count(i) != 0:
            dict[i] = stages.count(i) / l
            l -= stages.count(i)
        else:
            dict[i] = 0
    return sorted(dict, key=lambda x: dict[x], reverse = True )
    