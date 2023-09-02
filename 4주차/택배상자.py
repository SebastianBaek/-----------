# https://school.programmers.co.kr/learn/courses/30/lessons/131704
def solution(order):
    ans = 0
    main = list(range(1, len(order) + 1))
    main.reverse()
    temp = []
    order.reverse()

    while (order):
        if temp and temp[-1] == order[-1]:
            temp.pop()
            order.pop()
            ans += 1

        elif main:
            m = main.pop()
            if m == order[-1]:
                order.pop()
                ans += 1
            else:
                temp.append(m)
        else:
            break

    return ans
