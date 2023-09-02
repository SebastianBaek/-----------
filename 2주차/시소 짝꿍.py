# https://school.programmers.co.kr/learn/courses/30/lessons/152996
def solution(weights):
    ans = 0
    weights_dic = dict()
    for weight in weights:
        if weight in weights_dic:
            weights_dic[weight] += 1
        else:
            weights_dic[weight] = 1
    weights_items = sorted(weights_dic.items())
    print(weights_items)
    for key, value in weights_items:
        ans += value * (value - 1) // 2
        if key * 2 in weights_dic:
            ans += value * weights_dic[key * 2]
        if key * 3 / 2 in weights_dic:
            ans += value * weights_dic[key * 3 / 2]
        if key * 4 / 3 in weights_dic:
            ans += value * weights_dic[key * 4 / 3]
    return ans
