# https://school.programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations


def solution(numbers):
    comb = [list(set(permutations(numbers, i)))
            for i in range(1, len(numbers) + 1)]

    sieve = [True] * 10000000
    for i in range(2, 4000):
        if sieve[i]:
            for j in range(i * 2, 10000000, i):
                sieve[j] = False
    sieve[1] = False

    ans = 0
    for tuples in comb:
        for t in tuples:
            if t[0] != "0":
                temp = ""
                for num in t:
                    temp += num
                if sieve[int(temp)]:
                    ans += 1
    return ans
