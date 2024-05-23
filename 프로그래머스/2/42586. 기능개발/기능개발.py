def solution(progresses, speeds):
    answer = []
    for progress,speed in zip(progresses,speeds):
        need = 100-progress
        div,mod = divmod(need,speed)
        if mod == 0:
            answer.append(div)
        else:
            answer.append(div+1)
    
    dates = []
    cnt = 0
    dist = answer[0]
    for i in answer:
        if i <= dist:
            cnt += 1
        else:
            dates.append(cnt)
            cnt = 1
            dist = max(dist,i)
    dates.append(cnt)
    return dates