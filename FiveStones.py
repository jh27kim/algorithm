T = int(input())
answer = []


def check(board):
    for i in range(N):
        cntRow = 0
        cntCol = 0
        for j in range(N):
            if board[i][j] == "o":
                cntRow += 1
            else:
                if cntRow >= 5:
                    return True
                cntRow = 0

            if board[j][i] == "o":
                cntCol += 1
            else:
                if cntCol >= 5:
                    return True
                cntCol = 0

        if cntRow >= 5 or cntCol >= 5:
            return True

    return False


def checkDiag(board, start, dir):
    x, y = start
    if board[x][y] == "o":
        cnt = 1
    else:
        cnt = 0
    DIR = DIRECTION[dir]
    #print(start)

    while 0 <= x + DIR[0] < N and 0 <= y + DIR[1] < N:
        nx, ny = x + DIR[0], y + DIR[1]
        if board[nx][ny] == "o":
            cnt += 1
        else:
            if cnt >= 5:
                return True
            cnt = 0
        x, y = nx, ny
        #print(x, y, cnt)
    if cnt >= 5:
        return True
    return False


for i in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    if check(board):
        answer.append("YES")
        continue

    DIRECTION = [[1, 1], [-1, 1]]

    startLeft = [[i+1, 0] for i in range(N-5)] + [[0, 0]] + [[0, i+1] for i in range(N-5)]
    startRight = [[N-1-(i+1), 0] for i in range(N-5)] + [[N-1, 0]] + [[0, N-1-(i+1)] for i in range(N-5)]
    #print(startLeft, startRight)

    done = False
    for j in range(2*(N-5)+1):
        if checkDiag(board, startLeft[j], 0) or checkDiag(board, startRight[j], 1):
            answer.append("YES")
            done = True
            break
    if not done:
        answer.append("NO")

for i in range(1, T+1):
    print("#"+str(i), answer[i-1])


