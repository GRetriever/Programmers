def solution(s):
    ans = []
    for i in s:
        if ans and ans[-1] == i:
            ans.pop()
            continue
        else:
            ans.append(i)
    return 1 if not ans else 0