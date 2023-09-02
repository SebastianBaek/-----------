# https://school.programmers.co.kr/learn/courses/30/lessons/92342
ans = []


def dfs(shoots, arrow, apeach, info):
    if len(shoots) > 11:
        return
    elif arrow == 0:
        last = len(shoots) - 1
        while (len(shoots) != 11):
            shoots.append(0)

        ryon = 0
        for i in range(11):
            if shoots[i] > info[i]:
                ryon += 10 - i
                if info[i] != 0:
                    apeach -= 10 - i

        if ryon > apeach:
            ans.append((ryon - apeach, last, shoots))

    for i in range(arrow + 1):
        shoots_clone = shoots[:]
        shoots_clone.append(i)
        dfs(shoots_clone, arrow - i, apeach, info)


def solution(n, info):
    apeach = 0
    for i in range(11):
        if info[i] != 0:
            apeach += 10 - i
    dfs([], n, apeach, info)

    ans.sort(key=lambda x: (-x[0], -x[1], x[2]))
    return ans[0][2] if ans else [-1]
