def solution(board, h, w):
    answer = 0
    dir = [[-1,0],[0,1],[1,0],[0,-1]]
    for i,j in dir:
        if 0 <= h+i < len(board) and 0 <= w+j < len(board[0]):
            if board[h][w] == board[h+i][w+j]:
                answer += 1
    return answer