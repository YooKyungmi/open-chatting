from email import message


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."


def solution(record):
    data = {}
    ans = []
    words = ["님이 들어왔습니다.", "님이 나갔습니다."]
    for i in range(len(record)):
        line = record[i].split()

        if line[0] == "Change":
            data[line[1]] = line[2]

        elif line[0] == "Enter":
            data[line[1]] = line[2]
            ans.append((line[1], 0))
        else:
            ans.append((line[1], 1))

    answer = list(map(lambda x: data[x[0]]+words[x[1]], ans))

    return answer


print(solution(record))
