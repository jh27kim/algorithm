N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
MOVEMENT = [[1, -1], [1, 1], [1, 1], [1, -1]]
answer = int(1e9)


def district(x, y, d1, d2):
    new_board = [[0 for _ in range(N)] for _ in range(N)]
    start = [[x, y], [x, y], [x+d1, y-d1], [x+d2, y+d2]]
    loop = [d1, d2, d2, d1]

    for i in range(4):
        nx, ny = start[i]
        new_board[nx][ny] = 5

        for j in range(loop[i]):
            if 0 <= nx + MOVEMENT[i][0] < N and 0 <= ny + MOVEMENT[i][1] < N:
                nx += MOVEMENT[i][0]
                ny += MOVEMENT[i][1]
                new_board[nx][ny] = 5
            else:
                break

    for i in range(x+1, x+d1+d2):
        for j in range(N):
            if new_board[i][j] == 5:
                for k in range(j+1, N):
                    if new_board[i][k] == 5:
                        break
                    new_board[i][k] = 5
                break

    for i in range(N):
        for j in range(N):
            if new_board[i][j]:
                continue
            if 0 <= i < x+d1 and 0 <= j <= y:
                new_board[i][j] = 1
            elif 0 <= i <= x+d2 and y < j <= N-1:
                new_board[i][j] = 2
            elif x+d1 <= i <= N-1 and 0 <= j <y-d1+d2:
                new_board[i][j] = 3
            elif x+d2 < i <= N-1 and y-d1+d2 <= j <= N-1:
                new_board[i][j] = 4

    return new_board


for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if x + d1 + d2 >= N or y - d1 < 0 or y + d2 >= N:
                    continue

                #print(x, y, d1, d2)
                seperated_map = district(x, y, d1, d2)
                population = [0 for _ in range(5)]

                for r in range(N):
                    for c in range(N):
                        population[seperated_map[r][c]-1] += board[r][c]

                answer = min(answer, max(population) - min(population))

print(answer)
