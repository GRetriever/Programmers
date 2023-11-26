def solution(a, b, n):
    answer = 0
    n = n
    while n >= a:
        free_cola = (n // a) * b
        left_cola = n % a
        answer += free_cola
        n = left_cola + free_cola
    return answer