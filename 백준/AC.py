# https://www.acmicpc.net/problem/5430
from collections import deque

T = int(input())

for i in range(T):
    p = list(input())
    n = int(input())
    nums = input()[1:-1]
    if not nums:
        nums = []
    else:
        nums = nums.split(",")
    queue = deque(nums)
    reverse = False
    for move in p:
        if move == "D" and not queue:
            print("error")
            break
        elif move == "D" and reverse:
            queue.pop()
        elif move == "D" and not reverse:
            queue.popleft()
        elif move == "R":
            reverse = not reverse
    else:
        if reverse:
            queue.reverse()
        print("[" + ",".join(list(queue)) + "]")
