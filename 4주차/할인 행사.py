# https://school.programmers.co.kr/learn/courses/30/lessons/131127
def solution(want, number, discount):
    count_dic = dict()
    len_want = len(want)
    ans = 0
    for i in range(len_want):
        count_dic[want[i]] = 0

    for i in range(10):
        if discount[i] in count_dic:
            count_dic[discount[i]] += 1

    flag = True
    for j in range(len_want):
        if count_dic[want[j]] < number[j]:
            flag = False
            break

    if flag:
        ans += 1

    for i in range(10, len(discount)):
        if discount[i - 10] in count_dic:
            count_dic[discount[i - 10]] -= 1

        if discount[i] in count_dic:
            count_dic[discount[i]] += 1

        flag = True
        for j in range(len_want):
            if count_dic[want[j]] < number[j]:
                flag = False
                break

        if flag:
            ans += 1

    return ans
