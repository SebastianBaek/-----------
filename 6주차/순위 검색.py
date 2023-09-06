# https://school.programmers.co.kr/learn/courses/30/lessons/72412
def solution(info, query):
    info_dict = dict()
    for i in range(len(info)):
        content = info[i].split(" ")
        c = tuple(content[:-1])
        score = int(content[-1])
        if c in info_dict:
            info_dict[c].append(score)
        else:
            info_dict[c] = [score]

    ans = []
    dev = [["cpp", "java", "python"], ["backend", "frontend"],
           ["junior", "senior"], ["chicken", "pizza"]]

    for i in range(len(query)):
        success = 0
        q = query[i].split(" and ")
        food_score = q[-1].split(" ")
        q[-1] = food_score[0]
        key = [""]
        for j in range(4):
            temp = []
            if q[j] == "-":
                for k in range(len(key)):
                    sb = key.pop()
                    for m in dev[j]:
                        temp.append(sb + m + " ")
            else:
                for k in range(len(key)):
                    sb = key.pop()
                    temp.append(sb + q[j] + " ")
            key = temp
        for j in range(len(key)):
            if tuple(key[j].split(" "))[:-1] in info_dict:
                info_dict[tuple(key[j].split(" "))[:-1]].sort(reverse=True)
                for score in info_dict[tuple(key[j].split(" "))[:-1]]:
                    if score >= int(food_score[1]):
                        success += 1
                    else:
                        break
        ans.append(success)
    return ans
