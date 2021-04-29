class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution(S):
    opStack = ArrayStack()
    answer = ''
    for i in range(len(S)):
        if S[i].isalpha():
            answer += S[i]
        else:
            if S[i] == "(":
                opStack.push(S[i])

            elif S[i] == ")":
                while opStack.peek() != "(":
                    answer += opStack.pop()
                opStack.pop()

            elif prec[S[i]] > 1:
                while opStack.size() >= 1 and prec[opStack.peek()] >= prec[S[i]]:
                    answer += opStack.pop()
                opStack.push(S[i])


    while opStack.size():
        answer += opStack.pop()

    return answer


s = "(A+B)*(C+D)"
print(solution(s))