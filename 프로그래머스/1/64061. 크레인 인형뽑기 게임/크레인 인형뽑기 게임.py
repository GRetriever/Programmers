def solution(board, moves):
    answer = 0
    doll = []
    for i in moves:
        i -= 1
        for j in range(len(board)):
            if board[j][i] != 0:
                doll.append(board[j][i])
                board[j][i] = 0
                break
        if len(doll) > 1:
            if doll[-1] == doll[-2]:
                del doll[-2:]
                answer += 2
    return answer