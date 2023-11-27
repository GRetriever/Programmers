def solution(name, yearning, photo):
    answer = []
    for i in photo:
        nums = 0
        for j in i:
            if j in name:
                nums += yearning[name.index(j)]
        answer.append(nums)
    return answer