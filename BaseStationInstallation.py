def check(n, routers):
    return True if n <= routers else False


def solution(n, stations, w):
    answer = 0

    left, right = 0, n
    apartments = [0 for _ in range(n)]
    MOVEMENT = [1, -1]

    for s in stations:
        apartments[s - 1] = 1
        for i in range(1, w + 1):
            if s - 1 + i < n:
                apartments[s - 1 + i] = 1
            if s - 1 - i >= 0:
                apartments[s - 1 - i] = 1

    void = []
    temp = 0

    for i in apartments:
        if not i:
            temp += 1
        else:
            if temp:
                void.append(temp)
                temp = 0
    if temp:
        void.append(temp)

    n = 0
    for v in void:
        q, r = divmod(v, (w * 2 + 1))
        if r:
            n += (q + 1)
        else:
            n += q

    while left <= right:
        mid = (left + right) // 2
        if check(n, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


import math


def solution(n, stations, w):
    distance = []
    answer = 0
    for i in range(1, len(stations)):
        distance.append(stations[i]-1-w, stations[i-1]-w)

    distance.append(stations[i]-1-w)
    distance.append(n-stations[-1]+w)

    for d in distance:
        if d <= 0:
            continue
        answer += math.ceil(d/(w*2+1))
    return answer


