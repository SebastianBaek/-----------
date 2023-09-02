# https://school.programmers.co.kr/learn/courses/30/lessons/154540
from collections import deque


def solution(maps):
    ans = []
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    maps = [list(m) for m in maps]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if not maps[i][j].isalpha():
                food = int(maps[i][j])
                maps[i][j] = "X"
                queue = deque([(i, j)])
                while (queue):
                    x, y = queue.popleft()
                    for k in range(4):
                        dx, dy = x + d[k][0], y + d[k][1]
                        if -1 < dx < len(maps) and -1 < dy < len(maps[i]) and not maps[dx][dy].isalpha():
                            food += int(maps[dx][dy])
                            maps[dx][dy] = "X"
                            queue.append((dx, dy))
                ans.append(food)
    ans.sort()
    return [-1] if not ans else ans
