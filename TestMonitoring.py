N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
answer = 0

for i in range(N):
    if A[i] - B <= 0:
        answer += 1
        continue
    answer += 1
    q, r = divmod(A[i] - B, C)
    if r > 0:
        answer += (q+1)
    else:
        answer += q

print(answer)
