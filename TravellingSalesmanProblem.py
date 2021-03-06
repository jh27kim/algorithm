import sys

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
answer = sys.maxsize
VISITED_ALL = (1 << N) - 1
DP = [[None] * (1 << N) for _ in range(N)]


def find_path(last, visited):
    if visited == VISITED_ALL:
        return W[last][0] or sys.maxsize

    if DP[last][visited] is not None:
        return DP[last][visited]

    tmp = sys.maxsize
    for city in range(N):
        if visited & (1 << city) == 0 and W[last][city]:
            tmp = min(tmp, find_path(city, visited | (1 << city)) + W[last][city])

    DP[last][visited] = tmp
    return tmp


print(find_path(0, 1 << 0))
