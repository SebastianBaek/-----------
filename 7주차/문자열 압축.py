# https://school.programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    ans = 987654321
    for interval in range(1, 501):
        count = dict()
        count[s[:interval]] = [1]
        remain = 0
        for j in range(interval, len(s), interval):
            if j + interval > len(s):
                remain = s[j:]
                break
            if s[j - interval: j] == s[j: j + interval]:
                count[s[j: j + interval]][-1] += 1
            elif s[j: j + interval] in count:
                count[s[j: j + interval]].append(1)
            else:
                count[s[j: j + interval]] = [1]

        result = 0 if not remain else len(remain)
        for key, value in count.items():
            for times in value:
                if times == 1:
                    result += len(key)
                else:
                    result += len(str(times) + key)
        ans = min(ans, result)

    return ans
