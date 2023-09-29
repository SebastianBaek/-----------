# https://www.acmicpc.net/problem/7576
from collections import deque

M, N = map(int, input().split())
graph = []
queue = deque([])
blank = 0

for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(M):
        if row[j] == 1:
            queue.append((i, j))
        elif row[j] == -1:
            blank += 1

if len(queue) + blank == M * N:
    print(0)
else:
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while (queue):
        r, c = queue.popleft()
        for i in range(4):
            dr, dc = r + d[i][0], c + d[i][1]
            if -1 < dr < N and -1 < dc < M and graph[dr][dc] == 0:
                graph[dr][dc] = graph[r][c] + 1
                queue.append((dr, dc))
    ans = 0
    for i in range(N):
        if 0 in graph[i]:
            ans = -1
            break
        ans = max(ans, max(graph[i]))
    if ans != -1:
        print(ans - 1)
    else:
        print(ans)
