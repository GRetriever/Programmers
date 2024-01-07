def solution(keymap, targets):
    answer = []
    key = {}
    for i in keymap:
        for j,alp in enumerate(i):
            if (alp in key) and key[alp] < j+1:
                continue
            key[alp] = j+1
    for k in targets:
        total = 0
        for l in k:
            if l in key:
                total += key[l]
            else:
                total = -1
                break
        answer.append(total)
    return answer