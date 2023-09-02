# https://school.programmers.co.kr/learn/courses/30/lessons/154539
def solution(numbers):
    ans = [-1] * len(numbers)
    stacks = []
    for i in range(len(numbers)-1, -1, -1):
        for j in range(len(stacks)):
            if numbers[i] < stacks[-1]:
                ans[i] = stacks[-1]
                break
            else:
                stacks.pop()
        stacks.append(numbers[i])
    return ans
