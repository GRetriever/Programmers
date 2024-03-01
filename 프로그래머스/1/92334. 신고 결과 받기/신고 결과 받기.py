from collections import defaultdict
def solution(id_list, report, k):
    mail = {name:0 for name in id_list}
    # 신고 받은 수
    reports = defaultdict(int)
    # 신고한 수
    dict = defaultdict(list)
    for i in set(report):
        name,repo = i.split(' ')
        dict[name].append(repo)
        reports[repo] += 1
    
    reported_name = []
    for user,count in reports.items():
        if count >= k:
            reported_name.append(user)
    
    for a,b in dict.items():
        for name in reported_name:
            if name in b:
                mail[a] += 1
    
    return list(mail.values())