# https://school.programmers.co.kr/learn/courses/30/lessons/86052
ans = []


def dfs(i, d, visited, grid, now):
    length = 0
    while (True):
        dx, dy = now[0] + d[i % 4][0], now[1] + d[i % 4][1]
        if (dx, dy, i % 4) in visited:
            if length != 0:
                ans.append(length)
            break
        visited[(dx, dy, i % 4)] = True
        now = (dx % len(grid), dy % len(grid[0]))
        length += 1
        if grid[now[0]][now[1]] == "L":
            i -= 1
        elif grid[now[0]][now[1]] == "R":
            i += 1
    return visited


def solution(grid):
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = dict()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                visited = dfs(k, d, visited, grid, (i, j))
    ans.sort()
    return ans
