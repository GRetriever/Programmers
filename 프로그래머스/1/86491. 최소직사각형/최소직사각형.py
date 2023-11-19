def solution(sizes):
    x = []
    y = []
    for i in sizes:
        x.append(max(i))
        y.append(min(i))
    return max(x)*max(y)