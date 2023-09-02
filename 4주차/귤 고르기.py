# https://school.programmers.co.kr/learn/courses/30/lessons/138476
def solution(k, tangerine):
    ans = 0
    tangerine_dic = dict()
    for t in tangerine:
        if t in tangerine_dic:
            tangerine_dic[t] += 1
        else:
            tangerine_dic[t] = 1
    tangerine_values = list(tangerine_dic.values())

    tangerine_values.sort(reverse=True)
    for value in tangerine_values:
        k -= value
        ans += 1
        if k <= 0:
            break
    return ans
