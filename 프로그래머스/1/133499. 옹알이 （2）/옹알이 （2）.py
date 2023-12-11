def solution(babbling):
    pron = ['aya','ye','woo','ma']
    answer = 0
    for i in range(len(babbling)):
        for j in pron:
            if j*2 in babbling[i]:
                pass
            elif j in babbling[i]:
                babbling[i] = babbling[i].replace(j,'*')
        if all(char == '*' for char in babbling[i]):
            answer += 1
    return answer
    