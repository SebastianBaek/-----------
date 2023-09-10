# https://school.programmers.co.kr/learn/courses/30/lessons/42883
from itertools import combinations


def solution(number, k):
    stack = [number[0]]
    for i in range(1, len(number)):
        times = min(len(stack), k)
        if times == 0:
            stack += number[i:]
            break
        for j in range(times):
            if number[i] <= stack[-1]:
                break
            else:
                k -= 1
                stack.pop()
        stack.append(number[i])
    if k:
        for i in range(k):
            stack.pop()
    return "".join(stack)
