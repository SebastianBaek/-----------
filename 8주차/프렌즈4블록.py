# https://school.programmers.co.kr/learn/courses/30/lessons/17679
d = [(0, 1), (1, 0), (1, 1)]
score = 0


def rating(board):
    global score
    for i in range(len(board[0])):
        for j in range(1, len(board)):
            if board[j][i] == None:
                for k in range(j, 0, -1):
                    board[k][i], board[k - 1][i] = board[k - 1][i], board[k][i]

    score = 0
    for i in range(len(board)):
        score += board[i].count(None)

    return block_remove(board)


def block_remove(board):
    corner = []
    for i in range(len(board) - 1):
        for j in range(len(board[0]) - 1):
            if board[i][j]:
                for k in range(3):
                    di, dj = i + d[k][0], j + d[k][1]
                    if board[i][j] != board[di][dj]:
                        break
                else:
                    corner.append((i, j))

    if not corner:
        return

    for i in range(len(corner)):
        r, c = corner[i][0], corner[i][1]
        board[r][c] = None
        for i in range(3):
            dr, dc = r + d[i][0], c + d[i][1]
            board[dr][dc] = None

    return rating(board)


def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])

    block_remove(board)

    return score
