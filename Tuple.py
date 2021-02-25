def solution(s):
    s = s[1:-1]
    string = []
    for i in range(len(s)):
        if s[i] == "{":
            temp = []
            number = ""

        elif s[i] == "}":
            temp.append(int(number))
            string.append(temp)

        elif s[i] == "," and s[i+1].isdigit():
            temp.append(int(number))
            number = ""
        else:
            number += s[i]

    string.sort(key=lambda x: len(x))
    #print(string)
    res = set([string[0][0]])
    answer = [string[0][0]]
    #print('answer', answer)

    for j in range(1, len(string)):
        for n in set(string[j]) - res:
            answer.append(n)
            res.add(n)

    return answer


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))
