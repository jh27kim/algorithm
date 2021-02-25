T = int(input())
cube = [['www', 'www', 'www'],
        ['yyy', 'yyy', 'yyy'],
        ['rrr', 'rrr', 'rrr'],
        ['ooo', 'ooo', 'ooo'],
        ['ggg', 'ggg', 'ggg'],
        ['bbb', 'bbb', 'bbb']]

U, D, F, B, L, R = 0, 1, 2, 3, 4, 5
side_dict = {'U': 0, 'D': 1, 'F': 2, 'B': 3, "L": 4, "R": 5}


def rotate(ind, d):
    new_cube = cube.deepcopy(cube)
    new_arr = [[0 for _ in range(3)] for _ in range(3)]
    arr = cube[ind]

    if ind == 0:
        if d == '+':
            new_cube[F][0], new_cube[R][0], new_cube[B][0], new_cube[L][0] = cube[R][0], cube[B][0], cube[L][0], cube[F][0]
        else:
            new_cube[F][0], new_cube[R][0], new_cube[B][0], new_cube[L][0] = cube[L][0], cube[F][0], cube[R][0], cube[B][0]
    elif ind == 1:
        if d == '+':
            new_cube[F][2], new_cube[R][2], new_cube[B][2], new_cube[L][2] = cube[R][2], cube[B][2], cube[L][2], cube[F][2]
        else:
            new_cube[F][2], new_cube[R][2], new_cube[B][2], new_cube[L][2] = cube[L][2], cube[F][2], cube[R][2], cube[B][2]
    elif ind == 2:
        if d == '+':
            for i in range(3):
                new_cube[L][2-i][2] = cube[U][2][i]
                new_cube[D][2][i] = cube[L][i][2]
                new_cube[R][2-i][0] = cube[D][2][i]
                new_cube[U][2][i] = cube[R][i][0]
        elif d == '-':
            for i in range(3):
                cube[U][2][i] = new_cube[L][2-i][2]
                cube[L][i][2] = new_cube[D][2][i]
                cube[D][2][i] = new_cube[R][2-i][0]
                cube[R][i][0] = new_cube[U][2][i]

    elif ind == 3:
        if d == '+':
            for i in range(3):
                new_cube[L][2-i][0] = cube[U][0][i]
                new_cube[D][0][i] = cube[L][i][0]
                new_cube[R][2-i][2] = cube[D][0][i]
                new_cube[U][0][i] = cube[R][i][0]
        elif d == '-':
            for i in range(3):
                new_cube[U][0][i] = cube[L][2 - i][0]
                new_cube[L][i][0] = cube[D][0][i]
                new_cube[D][0][i] = cube[R][2 - i][2]
                new_cube[R][i][0] = cube[U][0][i]
    elif ind == 4:
        if d == '+':
            for i in range(3):
                new_cube[L][2 - i][0] = cube[U][0][i]
                new_cube[D][0][i] = cube[L][i][0]
                new_cube[R][2 - i][2] = cube[D][0][i]
                new_cube[U][0][i] = cube[R][i][0]
        elif d == '-':
            for i in range(3):
                cube[U][2][i] = new_cube[L][2 - i][2]
                cube[L][i][2] = new_cube[D][2][i]
                cube[D][2][i] = new_cube[R][2 - i][0]
                cube[R][i][0] = new_cube[U][2][i]
    elif ind == 5:
        if d == '+':
            for i in range(3):
                new_cube[L][2 - i][2] = cube[U][2][i]
                new_cube[D][2][i] = cube[L][i][2]
                new_cube[R][2 - i][0] = cube[D][2][i]
                new_cube[U][2][i] = cube[R][i][0]
        elif d == '-':
            for i in range(3):
                cube[U][2][i] = new_cube[L][2 - i][2]
                cube[L][i][2] = new_cube[D][2][i]
                cube[D][2][i] = new_cube[R][2 - i][0]
                cube[R][i][0] = new_cube[U][2][i]

    if d == '+':
        periphery = periphery[-1] + periphery[:-1]
        for i in range(3):
            for j in range(3):
                new_arr[j][3-1-i] = arr[i][j]

    else:
        periphery = periphery[1:] + periphery[0]
        for i in range(3):
            for j in range(3):
                new_arr[3-1-j][i] = arr[i][j]

    cube[ind] = new_arr






for _ in range(T):
    n = int(input())
    command = input().split()

    for c in command:
        side, direction = list(c)
        rotate(side_dict[side], direction)

    for row in cube[U]:
        print(row)
