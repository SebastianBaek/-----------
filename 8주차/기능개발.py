# https://school.programmers.co.kr/learn/courses/30/lessons/42586
import math


def solution(progresses, speeds):
    answer = []
    day = []
    for i in range(len(progresses)):
        day.append(math.ceil((100 - progresses[i]) / speeds[i]))
    cnt = 1
    m = day[0]
    for i in range(1, len(progresses)):
        if m < day[i]:
            answer.append(cnt)
            cnt = 1
            m = day[i]
        else:
            cnt += 1
    answer.append(cnt)
    return answer
