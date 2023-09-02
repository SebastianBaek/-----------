# https://school.programmers.co.kr/learn/courses/30/lessons/148653
def solution(storey):
    storey = list(map(int, list(str(storey))))
    ans = 0
    for i in range(len(storey)-1, 0, -1):
        if storey[i] < 5:
            ans += storey[i]
        elif storey[i] == 5:
            if storey[i-1] > 4:
                storey[i-1] += 1
            ans += 5
        else:
            storey[i-1] += 1
            ans += 10 - storey[i]
    ans += min(storey[0], 10 - storey[0] + 1)

    return ans
