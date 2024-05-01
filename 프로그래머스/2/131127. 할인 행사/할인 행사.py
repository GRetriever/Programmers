def solution(want, number, discount):
    answer = 0
    dict = {}
    for i,j in zip(want,number):
        dict[i] = j
    
    for i in range(len(discount)-9):
        shopping = discount[i:i+10]
        for j,k in dict.items():
            if shopping.count(j) < k:
                break
        else:
            answer += 1
        
    return answer