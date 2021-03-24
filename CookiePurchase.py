from itertools import combinations


def solution(cookie):
    answer = 0
    N = len(cookie)

    for k in range(N - 1):
        s1, s2 = k, k + 1
        first, second = cookie[s1], cookie[s2]
        i, j = s1, s2

        while True:
            if first < second:
                i -= 1
                if i >= 0:
                    first += cookie[i]
                else:
                    break
            elif first > second:
                j += 1
                if j < N:
                    second += cookie[j]
                else:
                    break
            else:
                answer = max(answer, first)
                if j + 1 < N:
                    j += 1
                    second += cookie[j]
                else:
                    break

    return answer