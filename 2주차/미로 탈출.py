# https://school.programmers.co.kr/learn/courses/30/lessons/159993
from collections import deque


def find_lever(queue, lever, maps, d):
    lever_time = 987654321
    row, column = len(maps), len(maps[0])
    while (queue):
        x, y, = queue.popleft()
        now = maps[x][y]
        if (x, y) == lever:
            lever_time = min(lever_time, now)
        for i in range(4):
            dx, dy = x + d[i][0], y + d[i][1]
            if -1 < dx < row and -1 < dy < column and maps[dx][dy] != "X":
                if type(maps[dx][dy]) == str:
                    maps[dx][dy] = now + 1
                elif now + 1 < maps[dx][dy]:
                    maps[dx][dy] = now + 1
                else:
                    continue
                queue.append((dx, dy))

    return lever_time


def find_exit(queue, exit, maps, d):
    exit_time = 987654321
    row, column = len(maps), len(maps[0])
    while (queue):
        x, y, = queue.popleft()
        now = maps[x][y]
        if (x, y) == exit:
            exit_time = min(exit_time, now)
        for i in range(4):
            dx, dy = x + d[i][0], y + d[i][1]
            if -1 < dx < row and -1 < dy < column and maps[dx][dy] != "X":
                if type(maps[dx][dy]) == str:
                    maps[dx][dy] = now + 1
                elif now + 1 < maps[dx][dy]:
                    maps[dx][dy] = now + 1
                else:
                    continue
                queue.append((dx, dy))

    return exit_time


def solution(maps):
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for i in range(len(maps)):
        maps[i] = list(maps[i])
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "L":
                lever = (i, j)
            elif maps[i][j] == "E":
                exit = (i, j)

    queue = deque([start])
    maps_clone = [m[:] for m in maps]
    maps[start[0]][start[1]] = 0
    maps_clone[lever[0]][lever[1]] = 0

    lever_time = find_lever(queue, lever, maps, d)
    queue = deque([lever])
    exit_time = find_exit(queue, exit, maps_clone, d)

    ans = lever_time + exit_time

    return -1 if ans > 987654321 else ans
