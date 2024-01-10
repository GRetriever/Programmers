def solution(numbers, hand):
    def cur_loc(num):
        keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
        for i in range(len(keypad)):
            for j in range(len(keypad[0])):
                if keypad[i][j] == num:
                    return (i,j)
    answer = ''
    l = cur_loc('*')
    r = cur_loc("#")
    for i in numbers:
        if i in (1,4,7):
            answer += 'L'
            l = cur_loc(i)
        elif i in (3,6,9):
            answer += 'R'
            r = cur_loc(i)
        else:
            l_dis = abs(l[0] - cur_loc(i)[0]) + abs(l[1] - cur_loc(i)[1])
            r_dis = abs(r[0] - cur_loc(i)[0]) + abs(r[1] - cur_loc(i)[1])
            
            if l_dis < r_dis:
                answer += 'L'
                l = cur_loc(i)
            elif l_dis > r_dis:
                answer += 'R'
                r = cur_loc(i)
            else:
                if hand == 'right':
                    answer += 'R'
                    r = cur_loc(i)
                else:
                    answer += 'L'
                    l = cur_loc(i)

    return answer