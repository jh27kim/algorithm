N, K = map(int, input().split())
A = list(map(int, input().split()))
robots = [0 for _ in range(N*2)]
answer = 1


def check(lst):
    cnt = 0
    for l in lst:
        if not l:
            cnt += 1

    return False if cnt >= K else True


while check(A):
    phase1, phase2, phase3 = False, False, False
    A = [A[-1]] + A[:-1]

    if robots[N-1]:
        robots[N-1] = 0

    for i in range(N-2, -1, -1):
        if robots[i] and not robots[i+1] and A[i+1] >= 1:
            robots[i+1] = 1
            robots[i] = 0
            A[i+1] -= 1

    if not robots[0] and A[0] >= 1:
        robots[0] = 1
        A[0] -= 1

    answer += 1

print(answer)
