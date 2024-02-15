def solution(X, Y):
    xy = set(X) & set(Y)
    
    if not xy:
        return '-1'
    if xy == {'0'}:
        return '0'
    
    answer = [i*min(X.count(i),Y.count(i)) for i in xy]
    return str(''.join(sorted(answer,reverse=True)))
    