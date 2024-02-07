def solution(a, b):
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    date = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    answer = date[(b+sum(months[:a-1]))%7]
    return answer