import sys

number = list(map(int, input().split()))
queue = []
answer = -10000
sys.setrecursionlimit(1000000)

board = [[i for i in range(1, 41) if i % 2 == 0],
         [13, 16, 19, 25, 30, 35, 40, 0],
         [22, 24, 25, 30, 35, 40, 0],
         [28, 27, 26, 25, 30, 35, 40, 0]]


def move():
    cur = [-1, -1, -1, -1]
    path = [[0, -1], [0, -1], [0, -1], [0, -1]]
    score = 0

    for i in range(10):
        #print(cur)
        pathNumber, position = path[queue[i]]

        if position + number[i] >= len(board[pathNumber]):
            path[queue[i]][1] = len(board[pathNumber]) - 1
            cur[queue[i]] = 0
            continue

        if position + number[i] in cur:
            return -1

        if cur[queue[i]] == 0:
            return -1

        score += board[pathNumber][position + number[i]]
        cur[queue[i]] = board[pathNumber][position + number[i]]
        path[queue[i]] = [pathNumber, position + number[i]]

        if cur[queue[i]] % 10 == 0 and cur[queue[i]] != 40:
            path[queue[i]][0] = cur[queue[i]] // 10
            path[queue[i]][1] = -1
    #print(cur)
    #print()
    return score


def comb(d):
    global answer
    if d == 10:
        answer = max(answer, move())
        return
    for i in range(4):
        queue.append(i)
        comb(d+1)
        queue.pop()

comb(0)
print(answer)
