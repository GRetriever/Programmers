def solution(board, h, w):
    answer = 0
    current_value = board[h][w]
    
    if h - 1 >= 0 and board[h - 1][w] == current_value:
        answer += 1
    if h + 1 < len(board) and board[h + 1][w] == current_value:
        answer += 1
    if w - 1 >= 0 and board[h][w - 1] == current_value:
        answer += 1
    if w + 1 < len(board[0]) and board[h][w + 1] == current_value:
        answer += 1

    return answer

#     answer = 0
#     move = [[-1,0],[1,0],[0,-1],[0,1]]
#     for i,j in move:
#         if h+i >= 0 and w+j >= 0 and board[h][w] == board[h+i][w+j]:
#             answer += 1
#     return answer