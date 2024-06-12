import sys

pair = {
    ")": "(",
    "]": "["
}

opposite = {
    ")": "[",
    "]": "("
}

point = {
    "(": 2,
    ")": 2,
    "[": 3,
    "]": 3,
}


def main():
    brackets = input()
    n = len(brackets)
    stack = []
    answer = 0
    points = 1
    for i in range(n):
        bracket = brackets[i]
        if bracket in "([":
            stack.append(bracket)
            points *= point[bracket]
        elif bracket in ")]":
            if not stack or stack[-1] == opposite[bracket]:
                answer = 0
                break
            if brackets[i-1] == pair[bracket]:
                answer += points
            stack.pop()
            points //= point[bracket]

    if stack:
        answer = 0
    print(answer)

    return 0


if __name__ == '__main__':
    main()
