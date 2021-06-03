def solution(n, k, cmd):
    answer = ''
    initial = [False] * n

    cur = k
    undo = []
    tail = n-1

    for comm in cmd:
        print(cur)
        if len(comm) > 1:
            command, number = comm.split(' ')
            idx = 0

            if command == 'D':
                for num in range(cur+1, n):
                    if not initial[num]:
                        idx += 1
                        if idx == int(number):
                            cur = num
                            break
            else:
                for num in range(cur-1, -1, -1):
                    if not initial[num]:
                        idx += 1
                        if idx == int(number):
                            cur = num
                            break
        else:
            if comm == 'C':
                initial[cur] = True
                undo.append(cur)

                if cur == tail:
                    for num in range(cur - 1, -1, -1):
                        if not initial[num]:
                            cur = num
                            break

                    #if cur == 1:
                    #    cur -= 1
                    tail = cur

                else:
                    for num in range(cur + 1, n):
                        if not initial[num]:
                            cur = num
                            break

            elif comm == 'Z':
                last = undo.pop()
                initial[last] = False
                if last > tail:
                    tail = last

    for i in initial:
        if i:
            answer += 'X'
        else:
            answer += 'O'

    return answer


n = 8
k = 3
cmd = ["C", "C", "C", "C", "C", "C", "C", "C"]
print(solution(n, k, cmd))