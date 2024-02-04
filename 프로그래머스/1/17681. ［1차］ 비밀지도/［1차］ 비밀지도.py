def solution(n, arr1, arr2):
    answer = []
    all = []
    for i,j in zip(arr1,arr2):
        map = bin(i|j)[2:]
        if len(map) < len(arr1):
            map = str(0)*(len(arr1) - len(map)) + map
        all.append(map)
    
    for i in all:
        i = i.replace('0',' ')
        i = i.replace('1','#')
        answer.append(i)
    return answer