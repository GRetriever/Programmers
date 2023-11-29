def solution(cards1, cards2, goal):
    answer = []
    for word in goal:
        if len(cards1) > 0 and word == cards1[0]:
            answer.append(word)
            cards1.remove(word)
        elif len(cards2) > 0 and word == cards2[0]:
            answer.append(word)
            cards2.remove(word)
    return 'Yes' if answer == goal else 'No'