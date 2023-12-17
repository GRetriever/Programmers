def solution(s, n):
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = []
    for i in s:
        if i == ' ':
            answer.append(' ')
        if i.isupper():
            new = (alp.find(i) + n) % 26
            answer.append(alp[new])
        elif i.islower():
            i = i.upper()
            new = (alp.find(i) + n) % 26
            answer.append(alp[new].lower())
    return ''.join(answer)