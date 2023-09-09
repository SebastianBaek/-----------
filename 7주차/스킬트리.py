# https://school.programmers.co.kr/learn/courses/30/lessons/49993
def solution(skill, skill_trees):
    ans = len(skill_trees)
    for tree in skill_trees:
        idx = dict()
        for i, alpha in enumerate(tree):
            idx[alpha] = i
        for i in range(len(skill) - 1, 0, -1):
            if skill[i] not in idx:
                continue
            elif skill[i-1] not in idx:
                ans -= 1
                break
            elif idx[skill[i-1]] > idx[skill[i]]:
                ans -= 1
                break
    return ans
