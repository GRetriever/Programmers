from collections import defaultdict,Counter
def solution(id_list, report, k):
    mail = {name:0 for name in id_list}

    dict = defaultdict(list)
    reported = defaultdict(int)
    for i in report:
        l,m = i.split(' ')
        if m not in dict[l]:
            dict[l].append(m)
            reported[m] += 1
        
    reported_id = []
    for user,count in reported.items():
        if int(count) >= int(k):
            reported_id.append(user)
    
    for x,y in dict.items():
        for h in reported_id:
            if h in y:
                mail[x] += 1
    return list(mail.values())