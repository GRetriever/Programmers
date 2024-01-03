def solution(players, callings):
    ranking = {player : i for i,player in enumerate(players)}
    for i in callings:
        current = ranking[i]
        ranking[i] -= 1
        ranking[players[current -1]] += 1
        
        players[current-1],players[current] = i,players[current-1]
    return players