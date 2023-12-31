def solution(data, ext, val_ext, sort_by):
    answer = []
    dict = {'code' : 0, 'date' : 1, 'maximum' : 2, 'remain' : 3}
    for i in data:
        if val_ext > i[dict[ext]]:
                answer.append(i)        
    sorted(answer, key = lambda x : x[dict[sort_by]])
    return sorted(answer, key = lambda x : x[dict[sort_by]])