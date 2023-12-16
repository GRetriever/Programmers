def solution(board, moves):
    answer = 0
    doll = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]:
                doll.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(doll) >= 2 and doll[-2] == doll[-1]:
            doll.pop()
            doll.pop()
            answer += 2
    return answer