def solution(new_id):
    answer = ''

    for i in range(len(new_id)):
        character = new_id[i]
        if character.isalpha():
            answer += character.lower()
        elif character.isdigit() or character == '-' or character == '_' or character == '.':
            answer += character

    new_answer = ""
    for i in range(len(answer)):
        if not new_answer:
            new_answer += answer[i]
            continue
        elif new_answer[-1] == '.' and answer[i] == '.':
            continue
        new_answer += answer[i]
    answer = new_answer

    if len(answer) >= 1:
        if answer[0] == '.' and len(answer) == 1:
            answer = ""
        elif answer[0] == '.' and len(answer) >= 1:
            answer = answer[1:]

    if len(answer) > 1:
        if answer[-1] == '.' and len(answer) == 1:
            answer = ""
        elif answer[-1] == '.' and len(answer) >= 1:
            answer = answer[:-1]

    if len(answer) == 0:
        answer += 'a'

    elif len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    while len(answer) <= 2:
        answer += answer[-1]

    return answer

new_id = "...b..."
print(solution(new_id))
