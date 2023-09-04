# https://school.programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    duplicated = dict()
    words = s.split(",")
    for word in words:
        number = word.lstrip("{").rstrip("}")
        if number in duplicated:
            duplicated[number] += 1
        else:
            duplicated[number] = 1

    items = sorted(duplicated.items(), key=lambda key_value: -key_value[1])
    ans = [int(key) for key, value in items]

    return ans
