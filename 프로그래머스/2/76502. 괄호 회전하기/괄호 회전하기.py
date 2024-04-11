def solution(s):
    answer = 0
    pair = {
        ')':'(',
        ']':'[',
        '}':'{'}
    for i in range(len(s)):
        cnt = []
        r = s[i:] + s[:i]
        for j in r:
            if j in (']','}',')'):
                if cnt and cnt[-1] == pair[j]:
                    cnt.pop()
                    continue
                else:
                    break
            cnt.append(j)
        else:
            if not cnt:
                answer += 1
    return answer