def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    
    s = ['.','-','_']
    id = ''
    for i in new_id:
        if i in s or i.isnumeric() or i.isalpha():
            id += i
    
    while '..' in id:
        id = id.replace('..','.')
    
    if id.startswith('.'):
        id = id[1:]
    if id.endswith('.'):
        id = id[:-1]
    
    if id == '':
        id = 'a'
    
    if len(id) >= 16:
        id = id[:15]
    if id.endswith('.'):
        id = id[:-1]
    
    while len(id) <= 2:
        id += id[-1]

    return id