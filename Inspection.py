N = int(input())
w = [int(input()) for _ in range(N)]
wd = [abs(w[i] - w[i+1]) for i in range(N-1)]


def gcd(n, m):
    return m if n%m == 0 else gcd(m, n%m)


def divisor(n):
    answer = [n]
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            answer.append(i)
            if n // i != i:
                answer.append(n // i)

    answer.sort()
    return answer


if len(wd) == 1:
    answer = wd[0]
else:
    answer = wd[0]
    for n in wd:
        answer = gcd(n, answer)

print(*divisor(answer), sep=" ")
