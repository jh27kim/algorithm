import heapq


def solution2(n, cores):
    answer = 0
    queue = []
    for i in range(len(cores)):
        heapq.heappush(queue, [cores[i], i])
        n -= 1
        if n == 0:
            return i + 1

    while n:
        procTime, coreNum = heapq.heappop(queue)
        procTime += cores[coreNum]
        heapq.heappush(queue, [procTime, coreNum])
        n -= 1

    return coreNum + 1


def solution(n, cores):
    answer = 0
    left = n // len(cores) * min(cores)
    right = n * min(cores)

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        avail = 0
        for core in cores:
            cnt += mid // core + 1
            if mid % core == 0:
                avail += 1
                cnt -= 1

        if cnt >= n:
            right = mid - 1

        elif cnt + avail < n:
            left = mid + 1

        else:
            for i in range(len(cores)):
                if mid % cores[i] == 0:
                    cnt += 1
                if cnt == n:
                    return i + 1


n = 6
cores = [1, 2, 3]
print(solution(n, cores))