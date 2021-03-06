def solution(n):
    answer = ''
    number = [1, 2, 4]
    i = 1
    digit = 1

    while True:
        i *= 3
        if n - i <= 0:
            break
        n -= i
        digit += 1
    n -= 1

    while digit:
        q, r = divmod(n, 3**(digit-1))
        answer += str(number[q])
        n = r
        digit -= 1
    return answer


n = 13
print(solution(n))