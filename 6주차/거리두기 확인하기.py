# https://school.programmers.co.kr/learn/courses/30/lessons/81302
ans = []


def search(now, d, place):
    for i in range(4):
        dr1 = now[0] + d[i][0]
        dc1 = now[1] + d[i][1]
        if -1 < dr1 < 5 and -1 < dc1 < 5:
            if place[dr1][dc1] == "P":
                return False
            else:
                for j in range(4):
                    if i + j == 3:
                        continue
                    dr2 = dr1 + d[j][0]
                    dc2 = dc1 + d[j][1]
                    if -1 < dr2 < 5 and -1 < dc2 < 5 and place[dr2][dc2] == "P":
                        if place[dr1][dc1] != "X":
                            return False
    return True


def room(place):
    result = True
    d = [(-1, 0), (0, 1), (0, -1), (1, 0)]

    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                result = search((i, j), d, place)
                if result == False:
                    ans.append(0)
                    return
    ans.append(1)
    return


def solution(places):
    for place in places:
        room(place)
    return ans
