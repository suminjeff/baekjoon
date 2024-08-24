import sys


if __name__ == '__main__':
    N = int(input())
    words = [input() for _ in range(N)]
    answer = 0
    for word in words:
        stack = []
        for i in range(len(word)):
            letter = word[i]
            if not stack:
                stack.append(letter)
            else:
                if stack[-1] == letter:
                    stack.pop()
                else:
                    stack.append(letter)
        if not stack:
            answer += 1
    print(answer)