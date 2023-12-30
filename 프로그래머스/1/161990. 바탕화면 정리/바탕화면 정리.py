def solution(wallpaper):
    x = []
    y = []
    for a,i in enumerate(wallpaper):
        for b,j in enumerate(i):
            if j == '#':
                x.append(a)
                y.append(b)
    return [min(x),min(y),max(x)+1,max(y)+1]