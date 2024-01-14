def solution(today, terms, privacies):
    answer = []
    dict = {}
    new_privacy = []
    for i in terms:
        j,k = i.split(' ')
        dict[j] = k
    for i in privacies:
        j,k = i.split(' ')
        exp = list(map(int,j.split('.')))
        exp[1] += int(dict[k])
        if exp[1] > 12:
            exp[0] += exp[1] // 12 if exp[1] % 12 != 0 else (exp[1] // 12) -1
            exp[1] = exp[1] % 12 if exp[1] % 12 != 0 else 12
        exp[2] -= 1
        new_privacy.append(exp)
    for i,privacy in enumerate(new_privacy):
        j,k,l = privacy
        year,month,day= list(map(int,today.split('.')))
        if year > j:
            answer.append(i+1)
            continue
        if year==j and month > k:
            answer.append(i+1)
            continue
        if year==j and month==k and day > l:
            answer.append(i+1)
            continue
    print(new_privacy)
    return answer
