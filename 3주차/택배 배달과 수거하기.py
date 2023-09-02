# https://school.programmers.co.kr/learn/courses/30/lessons/150369
def solution(cap, n, deliveries, pickups):
    ans = 0
    now = 0
    while (deliveries or pickups):
        arrs = [deliveries, pickups]
        for arr in arrs:
            while (arr):
                if arr[-1] == 0:
                    arr.pop()
                else:
                    break
        ans += max(len(deliveries), len(pickups)) * 2

        for arr in arrs:
            now = 0
            while (now != cap and arr):
                if now + arr[-1] <= cap:
                    now += arr.pop()
                else:
                    arr[-1] -= cap - now
                    now = cap
    return ans
