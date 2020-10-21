from collections import deque

dy = list(list() for i in range(10))
numbers = [3, 30, 34, 5, 9]
a = ''


# for i in numbers[::-1]:
#     a += str(i)
# print(a)

def digit(value, remain):
    if value <= 0:
        return remain
    return digit(value // 10, value % 10)


def solution(numbers):
    answer = ''
    for i in numbers:
        print(dy[digit(i, i)], i)
        dy[digit(i, i)].append(i)

    for j in dy[::-1]:
        if len(j) > 0:
            j.sort(key=lambda x: x * 3, reverse=True)
            answer += ''.join(map(str, j))

    return answer


def sortnum(num):
    max = int(''.join(map(str, num)))
    strt = 0
    end = len(num) - 1


def solutions(numbers):
    numbers = list(map(str, numbers))
    a = ['1', '2', '23', '13', '32', '20']
    print(numbers)
    # 왜지..?
    a.sort(key=lambda x: x * 2, reverse=True)
    b = '123'*3
    c = '1214'*3
    if (b > c):
        print('b 더큼')
    elif (b < c):
        print('c더큼')
    else:
        print('같음')
    print(a)
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))

def solutions(numbers):
    numbers = list(map(str, numbers))
    a = ['1', '2', '23', '13', '32', '20']
    a.sort(key=lambda x: x * 2, reverse=True)
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))



print(solutions(numbers))
# print(dy)
