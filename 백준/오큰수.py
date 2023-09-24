# https://www.acmicpc.net/problem/17298
N = int(input())
numbers = list(map(int, input().split()))

if N == 1:
    print(-1)
else:
    idx = N - 1
    temp = [0]
    ans = []
    for i in range(N - 1, -1, -1):
        while (temp):
            if numbers[i] < temp[-1]:
                ans.append(temp[-1])
                temp.append(numbers[i])
                break
            else:
                temp.pop()
        if not temp:
            temp.append(numbers[i])
            ans.append(-1)
    ans.reverse()
    for i in range(N):
        print(ans[i], end=" ")
