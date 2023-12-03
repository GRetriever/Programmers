def solution(n):
    a = '수박'
    if n % 2 == 0:
        return a*(n//2)
    if n % 2 == 1:
        return a*(n//2) + a[0]