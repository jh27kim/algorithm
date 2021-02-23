import copy

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
directions = [[[0], [1], [2], [3]],
              [[0, 2], [1, 3]],
              [[0, 1], [1, 2], [2, 3], [3, 0]],
              [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
              [[0, 1, 2, 3]]]

movement = [[-1, 0], [0, -1], [1, 0], [0, 1]]
visited = [[0 for _ in range(M)] for _ in range(N)]
answer = int(1e9)
import numpy as np

new_office = copy.deepcopy(office)


def check():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if new_office[i][j] == 0:
                cnt += 1

    return cnt


def scan(cam, direction, character):
    x, y = cam
    #print(direction)
    for d in direction:
        dx, dy = movement[d]
        nx = x + dx
        ny = y + dy
        while 0 <= nx < N and 0 <= ny < M and office[nx][ny] != 6:
            if office[nx][ny] == 0:
                new_office[nx][ny] += character
            nx += dx
            ny += dy


def dfs(x, y):
    global answer

    for i in range(x, N):
        #if i != x:
        #    y = 0
        for j in range(y, M):
            if 0 < office[i][j] < 6:
                cam_type = office[i][j]-1
                for d in range(len(directions[cam_type])):
                    scan([i, j], directions[cam_type][d], 1)
                    answer = min(answer, check())
                    print(i, j)
                    #print(np.asarray(new_office))
                    dfs(i, j+1)
                    scan([i, j], directions[cam_type][d], -1)


dfs(0, 0)
print(answer)
