# https://school.programmers.co.kr/learn/courses/30/lessons/86971
def dfs(wires):
    graph = [[] for i in range(len(wires) + 3)]
    visited = [False] * (len(wires) + 3)
    stack = []
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    for i in range(len(graph)):
        if graph[i]:
            stack.append(graph[i][0])
            while (stack):
                number = stack.pop()
                visited[number] = True
                for k in graph[number]:
                    if not visited[k]:
                        stack.append(k)
            break
    return abs(visited.count(True) - visited.count(False) + 1)


def solution(n, wires):
    ans = 987654321
    for i in range(len(wires)):
        wires_clone = [wire[:] for wire in wires]
        wires_clone.pop(i)
        ans = min(ans, dfs(wires_clone))

    return ans
