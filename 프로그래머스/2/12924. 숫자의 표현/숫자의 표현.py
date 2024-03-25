def solution(n):
    answer = 0
    start = 1
    total = 0
    while start <= n:
        for i in range(start,n+1):
            total += i
            if total == n:
                answer += 1
                start += 1
                total = 0
                break
            elif total > n:
                start += 1
                total = 0
                break
    return answer