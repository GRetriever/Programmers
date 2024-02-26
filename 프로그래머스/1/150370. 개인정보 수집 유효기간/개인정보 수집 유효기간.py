def solution(today, terms, privacies):
    answer = []
    
    dict = {}
    for term in terms:
        alp,month = term.split(' ')
        dict[alp] = int(month)
    
    for i,privacy in enumerate(privacies):
        date,alp = privacy.split(' ')
        date = list(map(int,date.split('.')))
        
        date[1] += dict[alp]
        if date[1] > 12:
            date[0] += date[1]//12 if date[1]%12 != 0 else (date[1]//12) - 1
            date[1] = date[1]%12 if date[1]%12 != 0 else 12
            
        date[2] -= 1
    
        year,month,day = list(map(int,today.split('.')))
        if year > date[0]:
            answer.append(i+1)
            continue
        if year == date[0] and month > date[1]:
            answer.append(i+1)
            continue
        if year == date[0] and month == date[1] and day > date[2]:
            answer.append(i+1)
            continue
            
    return answer