def changeSec(time):
    #print(time)
    H, M, S = time
    return int(H)*3600 + int(M)*60 + int(S)


def reverseSec(i):
    H, r1 = divmod(i, 3600)
    M, S = divmod(r1, 60)
    return '{:02d}:{:02d}:{:02d}'.format(H, M, S)


def solution(play_time, adv_time, logs):
    answer = ''
    adv_time = changeSec(adv_time.split(":"))
    play_time = changeSec(play_time.split(":"))
    intervals = [0 for _ in range(play_time)]
    start_time = [0]

    for l in logs:
        s, e = l.split('-')
        s = changeSec(s.split(":"))
        e = changeSec(e.split(":"))
        start_time.append(s)

        for i in range(s, e):
            intervals[i] += 1

    watch = 0
    start_time.append(play_time - adv_time)
    for i in start_time:
        temp = sum(intervals[i:i+adv_time])
        if temp > watch:
            watch = temp
            answer = reverseSec(i)
            print(temp)

    return answer


'''
    for l in logs:
        s, e = l.split('-')
        s = s.split(':')
        e = e.split(':')

        heapq.heappush(start, "".join(i for i in s))
        heapq.heappush(end, "".join(i for i in e))

    watch = 0
    while start and end:
        if start[0] < end[0]:
            watch += 1
            intervals.append((heapq.heappop(start), watch))
        else:
            watch -= 1
            intervals.append((heapq.heappop(end), watch))

    while end:
        watch -= 1
        intervals.append((heapq.heappop(end), watch))

    cumulative_watch = 0
    print(intervals)
    '''


play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]

print(solution(play_time, adv_time, logs))
