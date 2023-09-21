# https://school.programmers.co.kr/learn/courses/30/lessons/12905
def solution(board):
    if len(board) == 1:
        return board[0][0]
    d = [(-1, -1), (0, -1), (-1, 0)]
    ans = 0

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                temp = []
                for k in range(3):
                    dr, dc = i + d[k][0], j + d[k][1]
                    temp.append(board[dr][dc])
                if temp[0] == temp[1] == temp[2] >= 1:
                    board[i][j] = temp[0] + 1
                elif min(temp) >= 1:
                    board[i][j] = min(temp) + 1
                ans = max(ans, board[i][j])
    return ans ** 2
