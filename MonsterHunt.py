T = int(input())
res = []

for _ in range(T):
    D, L, N = map(int, input().split())
    # print(D, L, N)
    cnt = 0
    ans = 0

    while cnt < N:
        # print((1 + ((cnt * L) / 100)))
        ans += D * (1 + ((cnt * L) / 100))
        cnt += 1
        # print(D)

    res.append(int(ans))
for i in range(T):
    print("#" + str(i+1), res[i])

