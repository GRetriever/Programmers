def solution(keymap, targets):
    answer = []
    key = {}
    for i in keymap:
        for j,letter in enumerate(i):
            if letter in key and key[letter] < j+1:
                continue
            key[letter] = j+1
    for target in targets:
        total = 0
        for letter in target:
            if letter not in key:
                answer.append(-1)
                break
            total += key[letter]
        else:
            answer.append(total)
    
    return answer