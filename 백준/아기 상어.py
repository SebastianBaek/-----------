# https://www.acmicpc.net/problem/16236
from collections import deque

N = int(input())

graph = []
fishs = []

for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(N):
        if row[j] == 9:
            shark = (2, i, j)
            row[j] = 0
        elif row[j] > 0:
            fishs.append((row[j], i, j))

stack = 0
ans = 0
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while (True):
    visited = [[False] * N for i in range(N)]
    queue = deque([(shark[1], shark[2])])
    visited[shark[1]][shark[2]] = 0

    while (queue):
        r, c = queue.popleft()
        for i in range(4):
            dr, dc = r + d[i][0], c + d[i][1]
            if -1 < dr < N and -1 < dc < N and not visited[dr][dc] and graph[dr][dc] <= shark[0]:
                queue.append((dr, dc))
                visited[dr][dc] = visited[r][c] + 1

    eat = (400, 20, 20)
    for size, r, c in fishs:
        if not visited[r][c]:
            continue
        dist = visited[r][c]
        if size < shark[0] and dist < eat[0]:
            eat = (dist, r, c)
        elif size < shark[0] and dist == eat[0]:
            temp = [eat, (dist, r, c)]
            temp.sort(key=lambda X: (X[1], X[2]))
            eat = temp[0]

    if eat == (400, 20, 20):
        break

    stack += 1
    fishs.remove((graph[eat[1]][eat[2]], eat[1], eat[2]))
    if stack == shark[0]:
        shark = (shark[0] + 1, eat[1], eat[2])
        stack = 0
    else:
        shark = (shark[0], eat[1], eat[2])

    ans += eat[0]

print(ans)
