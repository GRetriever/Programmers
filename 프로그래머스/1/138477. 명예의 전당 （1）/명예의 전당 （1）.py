def solution(k, score):
    h = []
    a = []
    for num in score:
        h.append(num)
        
        if len(h) > k:
            h.remove(min(h))
            
        a.append(min(h))
        
    return a