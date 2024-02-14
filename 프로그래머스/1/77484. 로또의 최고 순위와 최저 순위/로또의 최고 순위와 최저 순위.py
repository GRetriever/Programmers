def solution(lottos, win_nums):
    ranking = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    lotto = set(lottos) & set(win_nums)
    l = len(lotto)
    z = lottos.count(0)
    return [ranking[l+z] , ranking[l]]