# https://school.programmers.co.kr/learn/courses/30/lessons/118667
from collections import deque


def solution(queue1, queue2):
    q1, q2 = 0, 0
    q_max = 0
    for i in range(len(queue1)):
        q1 += queue1[i]
        q2 += queue2[i]
        q_max = max(q_max, queue1[i], queue2[i])

    if (q1 + q2) % 2 == 1 or q_max > q1 + q2 - q_max:
        return -1
    if q1 == q2:
        return 0

    ans = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    target = (q1 + q2) // 2
    q1_count, q2_count = 0, 0
    floor = len(queue1)
    while (target != q1):
        if q1 < q2:
            num = queue2.popleft()
            q1 += num
            q2 -= num
            queue1.append(num)
            ans += 1
            q2_count += 1
        else:
            num = queue1.popleft()
            q2 += num
            q1 -= num
            queue2.append(num)
            ans += 1
            q1_count += 1

        if q1_count == floor * 2 or q2_count == floor * 2:
            return -1
    return ans
