import sys

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
DP = [[1 if i == j else 0 for j in range(N)] for i in range(N)]


def check(lst):
    if lst == lst[::-1]:
        return True
    return False


for i in range(N-1):
    if numbers[i] == numbers[i+1]:
        DP[i][i+1] = 1

for i in range(1, N):
    for j in range(1, i+1):
        if numbers[i] == numbers[i-j] and DP[i-j+1][i-1]:
            DP[i-j][i] = 1

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(DP[s-1][e-1])
