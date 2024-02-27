def solution(players, callings):
    ranking = {player : i for i,player in enumerate(players)}
    for i in callings:
        cur = ranking[i]
        ranking[i] -= 1
        ranking[players[cur-1]] += 1
        
        players[cur-1],players[cur] = i,players[cur-1]
    return players  