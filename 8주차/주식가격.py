# https://school.programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
    ans = [0] * len(prices)
    stack = []
    for idx, price in enumerate(prices):
        while (stack and stack[-1][1] > price):
            i, value = stack.pop()
            ans[i] = idx - i
        stack.append((idx, price))

    for idx, price in stack:
        ans[idx] = len(prices) - idx - 1
    return ans
