from collections import deque

N, K = map(int, input().split())

queue = deque()
queue.append(N)
SIZE = 100001
visited = [0] * 100001
visited[N] = 1
answer = 0

while queue:
    lenq = len(queue)
    while lenq:
        x = queue.popleft()
        if x == K:
            print(answer)
            exit()

        if x + 1 < SIZE:
            if not visited[x+1]:
                visited[x+1] = 1
                queue.append(x+1)
        if x - 1 >= 0 and not visited[x-1]:
            if not visited[x-1]:
                visited[x-1] = 1
                queue.append(x-1)
        if 2 * x < SIZE:
            if not visited[2*x]:
                visited[x+1] = 1
                queue.append(2 * x)
        lenq -= 1
    answer += 1
