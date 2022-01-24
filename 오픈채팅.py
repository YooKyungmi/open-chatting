record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."


def solution(record):
    data = {}
    answer = []
    for i in range(len(record)):
        list = record[i].split()
        if list[0] == "Change":
            data[list[1]] = list[2]

        elif list[0] == "Enter":
            data[list[1]] = list[2]
            ans = "{0}님이 들어왔습니다.".format(data[list[1]])
            answer.append(ans)

        else:
            ans = "{0}님이 나갔습니다.".format(data[list[1]])
            answer.append(ans)

    return answer


print(solution(record))
