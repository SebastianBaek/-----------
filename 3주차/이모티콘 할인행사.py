# https://school.programmers.co.kr/learn/courses/30/lessons/150368
result = []


def sales(users, emoticons, idx, cost):
    if idx == len(emoticons):
        plus = 0
        profit = 0
        for u_rate, u_price in users:
            temp = 0
            for e_rate, e_price in cost:
                if u_rate <= e_rate:
                    temp += e_price
            if u_price <= temp:
                plus += 1
            else:
                profit += temp
        result.append([plus, profit])

        return

    for i in range(1, 5):
        cost.append([i * 10, emoticons[idx] * (10 - i) / 10])
        sales(users, emoticons, idx + 1, cost)
        cost.pop()
    return


def solution(users, emoticons):
    sales(users, emoticons, 0, [])
    result.sort(key=lambda x: (-x[0], -x[1]))

    return result[0]
