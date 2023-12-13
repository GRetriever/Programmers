def solution(X, Y):
    answer = []
    com = (set(X) & set(Y))
    if not com:
        return '-1'
    elif len(com) == 1 and'0' in com:
        return '0'
    else:
        result = [i*min(X.count(i),Y.count(i)) for i in com]
        return ''.join(sorted(result,reverse=True))