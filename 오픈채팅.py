record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."

# 런타임 오류


def solution(record):
    data = {}
    answer = []
    for i in range(len(record)):
        list = record[i].split()
        answer.append(list[1])

        if list[0] == "Change":
            data[list[1]] = list[2]
            answer.pop()

        elif list[0] == "Enter":
            data[list[1]] = list[2]

    for j in range(len(record)):
        if record[j][0] == 'E':
            ans = "{0}님이 들어왔습니다.".format(data[answer[j]])
            answer[j] = ans

        elif record[j][0] == 'L':
            ans = "{0}님이 나갔습니다.".format(data[answer[j]])
            answer[j] = ans

    return answer


print(solution(record))
