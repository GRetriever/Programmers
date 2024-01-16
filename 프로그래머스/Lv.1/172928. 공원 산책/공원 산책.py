def solution(park, routes):
    h = len(park)
    w = len(park[0])
    news = {'E' : [0,1] , 'W' : [0,-1] , 'S' : [1,0] , 'N' : [-1,0]}
    loc = []
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                loc = [i,j]
    for route in routes:
        dir,move = route.split(' ')
        y = loc[0]
        x = loc[1]
        ok = 0
        for _ in range(int(move)):
            x += news[dir][1]
            y += news[dir][0]
            if y >= h or x >= w or y < 0 or x < 0 or park[y][x] == 'X':
                ok += 1
                break
        if ok == 0:
            loc[0] += news[dir][0] * int(move)
            loc[1] += news[dir][1] * int(move)
    return loc