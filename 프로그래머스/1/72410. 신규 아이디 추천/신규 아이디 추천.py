def solution(new_id):
    new_id = new_id.lower()
    
    s = ['-','_','.']
    id = ''
    for i in new_id:
        if i.isnumeric() or i.isalpha() or i in s:
            id += i
    
    while '..' in id:
        id = id.replace('..','.')
    
    if id.startswith('.'):
        id = id[1:]
    if id.endswith('.'):
        id = id[:-1]
    
    if id == '':
        id = 'a'
    
    if len(id) > 15:
        id = id[:15]
    if id.endswith('.'):
        id = id[:-1]
    
    while len(id) <= 2:
        id += id[-1]
    
    return id