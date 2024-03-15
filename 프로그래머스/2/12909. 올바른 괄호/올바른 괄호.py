def solution(s):
    if s.startswith(')') or s.endswith('('):
        return False
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            return False
    if cnt == 0:
        return True
    return False