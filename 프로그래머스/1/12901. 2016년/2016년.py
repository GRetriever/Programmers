def solution(a, b):
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    cnt = 0
    cnt += sum(months[:a-1])
    cnt += b-1
    date = days[cnt%7]
    return date