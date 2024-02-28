def solution(park, routes):
    dict = {'E':[0,1],'S':[1,0],'W':[0,-1],'N':[-1,0]}
    loc = []
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                loc = [i,j]
                break
    
    for route in routes:
        dir,move = route.split(' ')
        y = loc[0]
        x = loc[1]
        ok = 0
        for _ in range(int(move)):
            y += dict[dir][0]
            x += dict[dir][1]
            if y >= len(park) or x >= len(park[0]) or y < 0 or x < 0 or park[y][x] == 'X':
                ok += 1
                break
        if ok == 0:
            loc[0] += dict[dir][0] * int(move)
            loc[1] += dict[dir][1] * int(move)
            
    return loc