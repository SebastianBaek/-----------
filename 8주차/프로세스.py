# https://school.programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    sequence = []
    priorities_set = sorted(list(set(priorities)), reverse=True)

    last = 0
    for i in priorities_set:
        temp = last
        for j in range(len(priorities)):
            if priorities[(temp + j) % len(priorities)] == i:
                sequence.append((temp + j) % len(priorities))
                last = (temp + j) % len(priorities)

    return sequence.index(location) + 1
