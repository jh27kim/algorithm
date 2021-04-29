import math

answer = 0


def dfs(sieve, n, depth, visited, queue, x):
    global answer

    if depth == 3:
        if sum(queue) == n:
            answer += 1
            return

    for i in range(x, len(sieve)):
        if sieve[i] and not visited[i]:
            visited[i] = True
            queue.append(i)
            dfs(sieve, n, depth + 1, visited, queue, i+1)
            queue.pop()
            visited[i] = False


def solution(n):
    global answer
    sieve = [True for _ in range(n + 1)]
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            idx = i
            while idx + i <= n:
                idx += i
                sieve[idx] = False

    visited = [0 for _ in range(n + 1)]
    queue = []
    dfs(sieve, n, 0, visited, queue, 1)


    return answer


n = 33
print(solution(n))