# https://school.programmers.co.kr/learn/courses/30/lessons/43165
from itertools import product


def solution(numbers, target):
    ans = 0

    for i in product(["-", "+"], repeat=len(numbers)):
        result = 0
        for j in range(len(i)):
            if i[j] == "-":
                result -= numbers[j]
            else:
                result += numbers[j]
        if result == target:
            ans += 1
    return ans
