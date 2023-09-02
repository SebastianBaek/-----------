# https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations


def solution(k, dungeons):
    length = len(dungeons)
    ans = 0

    for sequence in permutations(range(length), length):
        piro = k
        result = 0
        for i in sequence:
            if dungeons[i][0] <= piro:
                piro -= dungeons[i][1]
                result += 1
            else:
                break
        ans = max(ans, result)
    return ans
