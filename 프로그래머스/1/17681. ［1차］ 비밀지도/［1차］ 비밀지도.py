def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        map = bin(i|j)[2:]
        if len(map) < n:
            map = str(0)*(n-len(map)) + map
        map = map.replace('0',' ').replace('1','#')
        answer.append(map)
    return answer