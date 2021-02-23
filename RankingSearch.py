def solution(info, query):
    candidates = []
    answer = []
    for i in info:
        candidates.append(i.split(' '))

    for q in query:
        valid = [1 for _ in range(len(info))]
        new_q = q.split(' ')
        new_q = [s for s in new_q if s != 'and']
        ind = -1
        for j in range(len(new_q)):
            ind += 1
            if new_q[j] == 'and' or new_q[j] == '-':
                continue
            for k in range(len(candidates)):
                #print(candidates[k], new_q[j], valid)
                if valid[k]:
                    if new_q[j].isdigit():
                        if int(candidates[k][ind]) < int(new_q[j]):
                            valid[k] = 0
                    else:
                        if candidates[k][ind] != new_q[j]:
                            valid[k] = 0

        answer.append(sum(valid))

    return answer


info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

print(solution(info, query))
