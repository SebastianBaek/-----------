# https://school.programmers.co.kr/learn/courses/30/lessons/76502
from collections import deque


def solution(s):
    ans = 0
    str_list = ["[", "]", "{", "}", "(", ")"]
    s = deque(s)

    for i in range(len(s)):
        s.append(s.popleft())
        size = [0, 0, 0]
        recent = []
        result = True
        for j in range(len(s)):
            for k in range(6):
                if s[j] == str_list[k] and k % 2 == 0:
                    size[k // 2] += 1
                    recent.append(s[j])
                    break
                elif s[j] == str_list[k] and k % 2 == 1:
                    size[k // 2] -= 1
                    if not recent or recent.pop() != str_list[k - 1]:
                        result = False
                    break
            if -1 in size:
                result = False
                break
        if any(size):
            result = False
        if result:
            ans += 1
    return ans
