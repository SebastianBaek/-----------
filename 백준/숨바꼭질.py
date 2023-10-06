# https://www.acmicpc.net/problem/1697
from collections import deque

n, k = map(int, input().split())

d = ["+1", "-1", "*2"]
visited = [False] * 100001
visited[n] = True
queue = deque([(n, 0)])
ans = 987654321

while (queue):
    x, now = queue.popleft()
    if x == k:
        ans = min(ans, now)
        continue
    for i in range(3):
        dx = eval(str(x) + d[i])
        if -1 < dx < 100001 and not visited[dx]:
            queue.append((dx, now + 1))
            visited[dx] = True
print(ans)
