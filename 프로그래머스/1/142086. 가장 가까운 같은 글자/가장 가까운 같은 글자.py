def solution(s):
    answer = []
    word = {}
    for i,alp in enumerate(s):
        if alp not in word:
            answer.append(-1)
        else:
            answer.append(i-word[alp])
        word[alp] = i
    return answer