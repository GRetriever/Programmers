def solution(wallpaper):
    y = []
    x = []
    for i,row in enumerate(wallpaper):
        for j,ele in enumerate(row):
            if ele == '#':
                y.append(i)
                x.append(j)
    return [min(y),min(x),max(y)+1,max(x)+1]