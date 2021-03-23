import sys


def bfs(v, color, visited):
    q = [v]
    color[v] = 1
    visited[v] = 1

    while q:
        x = q.pop()
        for y in adj_lst[x]:
            if not visited[y]:
                visited[y] = 1
                color[y] = 3 - color[x]
                q.append(y)
            else:
                if color[y] == color[x]:
                    return False
        #print(x, color)

    return True


for _ in range(int(sys.stdin.readline())):
    V, E = map(int, input().split())
    adj_lst = [[] for _ in range(V+1)]
    color = [0 for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for e in range(E):
        a, b = map(int, input().split())
        adj_lst[a].append(b)
        adj_lst[b].append(a)

    flag = True
    for v in range(1, V+1):
        if not visited[v]:
            if not bfs(v, color, visited):
                flag = False
    #print(color)

    if flag:
        print('YES')
    else:
        print('NO')
