def solution(lottos, win_nums):
    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    answer = []
    num = 0
    for i in lottos:
        if i != 0 and i in win_nums:
            num += 1
    answer.append(rank[num])
    answer.append(rank[num+lottos.count(0)])
    return sorted(answer)