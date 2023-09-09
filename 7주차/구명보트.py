# https://school.programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    ans = len(people)
    while (left < right):
        big = people[right]
        small = people[left]
        if big + small <= limit:
            ans -= 1
            left += 1
        right -= 1
    return ans
