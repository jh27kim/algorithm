import sys

N, start, end, M = map(int, input().split())
adj_lst = [[] for _ in range(N)]
MAX = sys.maxsize
distance = [-MAX for _ in range(N)]
salary = list(map(int, input().split()))
distance[start] = salary[start]




def BF():
    for i in range(N+1):
        if distance[end] == -MAX and i == N:
            print('gg')
            return
        for src in range(N):
            for dest, cost in adj_lst[src]:
                if distance[src] == MAX:
                    continue
                if distance[dest] > distance[src] + cost:
                    distance[dest] = distance[src] + cost
                    if i == N:
                        if check(E):
                            print('gee')
                            return False
    return True


for _ in range(M):
    a, b, cost = map(int, input().split())
    adj_lst[a].append([b, cost])

for i in range(len(salary)):
    for j in range(len(adj_lst[i])):
        for k in range(len(salary)):
            if adj_lst[i][j][0] == k:
                adj_lst[i][j][1] = salary[k] - adj_lst[i][j][1]

if BF():
    print(distance[end])
