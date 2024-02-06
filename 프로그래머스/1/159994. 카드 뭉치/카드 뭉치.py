def solution(cards1, cards2, goal):
    deck1 = 0
    deck2 = 0
    for i in goal:
        if deck1 < len(cards1) and cards1[deck1] == i:
            deck1 += 1
        elif deck2 < len(cards2) and cards2[deck2] == i:
            deck2 += 1
        else:
            return 'No'
    return 'Yes'