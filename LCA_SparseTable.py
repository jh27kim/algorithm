input = __import__('sys').stdin.readline
m = int(input())
f = [0] + list(map(int, input().split()))
DP = [[f[i]] for i in range(m+1)]

for j in range(1, 20):
    for i in range(1, m+1):
        DP[i].append(DP[DP[i][j-1]][j-1])

q = int(input())
for _ in range(q):
    n, x = map(int, input().split())
    for j in range(19, -1, -1):
        if n >= 1 << j:
            n -= 1 << j
            x = DP[x][j]

    print(x)