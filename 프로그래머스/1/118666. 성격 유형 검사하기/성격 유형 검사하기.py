def solution(survey, choices):
    from collections import defaultdict
    answer = ''
    dict = defaultdict(int)
    char = ['RT','CF','JM','AN']
    score = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    for i,j in zip(survey,choices):
        if j <= 3:
            dict[i[0]] += score[j]
        elif j >= 4:
            dict[i[1]] += score[j]
    for i in char:
        if dict[i[0]] == dict[i[1]]:
            answer += sorted(i)[0]
        elif dict[i[0]] > dict[i[1]]:
            answer += i[0]
        elif dict[i[0]] < dict[i[1]]:
            answer += i[1]
    return answer