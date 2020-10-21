commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
array = [1, 5, 2, 6, 3, 7, 4]


def solution(array, commands):
    answer = []
    for c in range(len(commands)):
        i = commands[c][0]
        j = commands[c][1]
        k = commands[c][2]
        arr = array[i - 1:j]

        arr.sort()
        answer.append(arr[k - 1])
    return answer


print(solution(array, commands))
