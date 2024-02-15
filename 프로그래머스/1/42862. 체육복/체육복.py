def solution(n, lost, reserve):
    # 자기 옷
    my = set(reserve) & set(lost)
    reserve = set(reserve) - set(my)
    lost = set(lost) - set(my)
    
    # 빌리기
    for i in reserve:
        f = i-1
        b = i+1
        if f in lost:
            lost.remove(f)
        elif b in lost:
            lost.remove(b)
    
    return n-len(lost)