# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque


def solution(maps):
    visited = [[] for i in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 1:
                visited[i].append(float("inf"))
            else:
                visited[i].append("X")

    d = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    queue = deque([(0, 0)])
    visited[0][0] = 1

    while (queue):
        r, c = queue.popleft()
        for i in range(4):
            dr, dc = r + d[i][0], c + d[i][1]
            if -1 < dr < len(maps) and -1 < dc < len(maps[0]) \
                    and visited[dr][dc] != "X" and visited[dr][dc] > visited[r][c] + 1:
                visited[dr][dc] = visited[r][c] + 1
                queue.append((dr, dc))

    return -1 if visited[-1][-1] == float("inf") else visited[-1][-1]
