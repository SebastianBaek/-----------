# https://school.programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations


def solution(orders, course):
    count = dict()
    for order in orders:
        for i in range(len(course)):
            if len(order) >= course[i]:
                comb = combinations(order, course[i])
                for j in comb:
                    key = "".join(sorted(j))
                    if key in count:
                        count[key] += 1
                    else:
                        count[key] = 1
    frequency = dict()
    items = count.items()
    for key, value in items:
        if value < 2:
            continue

        if len(key) not in frequency:
            frequency[len(key)] = [(key, value)]
        else:
            if frequency[len(key)][0][1] < value:
                frequency[len(key)] = [(key, value)]
            elif frequency[len(key)][0][1] == value:
                frequency[len(key)].append((key, value))

    ans = []
    for i in frequency.values():
        for j in i:
            ans.append(j[0])
    ans.sort()
    return ans
