# https://school.programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    queue = deque([])
    ans = 0

    for i in range(len(cities)):
        if cities[i].upper() in queue:
            ans += 1
            queue.remove(cities[i].upper())
        else:
            ans += 5
            if len(queue) >= cacheSize:
                queue.popleft()
        queue.append(cities[i].upper())

    return ans
