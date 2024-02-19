def solution(ingredient):
    answer = 0
    burger = []
    for i in ingredient:
        burger.append(i)
        if burger[-4:] == [1,2,3,1]:
            answer += 1
            del burger[-4:]
    return answer