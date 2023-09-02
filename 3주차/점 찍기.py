# https://school.programmers.co.kr/learn/courses/30/lessons/140107
def solution(k, d):
    dots = 0
    for y in range(0, d + 1, k):
        dots += pow(pow(d, 2) - pow(y, 2), 1/2) // k + 1
    return dots
