def solution(k, tangerine):
    from collections import Counter
    answer = 0
    total = 0
    dict = Counter(tangerine)
    sort_dict = sorted(dict.items(),key=lambda x: x[1],reverse=True)
    for i in sort_dict:
        total += i[1]
        answer += 1
        if total >= k:
            return answer
    return answer