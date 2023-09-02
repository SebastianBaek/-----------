# https://school.programmers.co.kr/learn/courses/30/lessons/131130
def solution(cards):
    groups = []
    idx_dic = dict()

    for i in range(len(cards)):
        group = []
        idx = cards[i] - 1

        while (idx not in idx_dic):
            idx_dic[idx] = True
            group.append(idx)
            idx = cards[idx] - 1

        if group:
            groups.append(group)

    groups.sort(key=len, reverse=True)

    return 0 if len(groups) < 2 else len(groups[0]) * len(groups[1])
