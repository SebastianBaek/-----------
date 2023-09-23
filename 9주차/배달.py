# https://school.programmers.co.kr/learn/courses/30/lessons/12978
from heapq import heappush, heappop


def solution(N, road, K):
    graph = [[] for i in range(N + 1)]
    for i in range(len(road)):
        a, b, c = road[i]
        graph[a].append((b, c))
        graph[b].append((a, c))

    dist = [987654321] * (N + 1)
    heap = []
    heappush(heap, (0, 1))
    dist[1] = 0

    while (heap):
        d, now = heappop(heap)
        if dist[now] < d:
            continue
        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heappush(heap, (cost, i[0]))

    ans = 0
    for d in dist:
        if d <= K:
            ans += 1
    return ans
