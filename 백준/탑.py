# https://www.acmicpc.net/problem/2493
N = int(input())
towers = list(map(int, input().split()))

if N == 1:
    print(0)
else:
    stack = []
    ans = []
    for idx, tower in enumerate(towers):
        while (stack and stack[-1][1] < tower):
            stack.pop()

        if not stack:
            ans.append(0)
        else:
            ans.append(stack[-1][0] + 1)

        stack.append((idx, tower))
    for i in ans:
        print(i, end=" ")
