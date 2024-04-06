def solution(arr):
    num = 1
    while True:
        lcm = max(arr) * num
        cnt = 0
        for i in arr:
            if lcm % i !=0:
                break
            else:
                cnt += 1
        if cnt == len(arr):
            return lcm
        else:
            num += 1