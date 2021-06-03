def solution(s):
    answer = ""
    embedding = dict()
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for n in range(10):
        embedding[numbers[n]] = n

    stack = []
    for l in s:
        print(l)
        if l.isdigit():
            answer += l
        else:
            stack.append(l)
            if "".join(stack) in embedding:
                answer += str(embedding["".join(stack)])
                stack = []


    return int(answer)


s = "one4seveneight"
print(solution(s))