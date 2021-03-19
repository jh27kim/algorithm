import sys

N = int(input())
population = list(map(int, sys.stdin.readline().split()))
adj_lst = [[] for _ in range(N)]
sys.setrecursionlimit(10000)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    adj_lst[a-1].append(b-1)
    adj_lst[b-1].append(a-1)


visited = [0 for _ in range(N)]
DP = [[[0 for _ in range(N)]]]
answer = 0


def dfs(x, queue):
    global answer

    if len([x for x in visited if x != 0]) == N:
        temp = 0
        for l in queue:
            temp += population[l]
        answer = max(answer, temp)
        return

    for i in range(x, N):
        if not visited[i]:
            visited[i] += 1
            for j in adj_lst[i]:
                visited[j] += 1
            queue.append(i)
            dfs(i+1, queue)
            queue.pop()
            visited[i] -= 1
            for j in adj_lst[i]:
                visited[j] -= 1


dfs(0, [])
print(answer)
