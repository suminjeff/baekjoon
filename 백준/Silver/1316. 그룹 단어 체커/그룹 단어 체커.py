def check(word):
    stack = []
    top = -1
    for letter in word:
        if stack:
            if letter in stack:
                if stack[top] == letter:
                    stack.append(letter)
                    top += 1
                else:
                    return 0
            else:
                stack.append(letter)
                top += 1
        else:
            stack.append(letter)
            top += 1
    return 1


N = int(input())
ans = 0
for _ in range(N):
    word = input()
    ans += check(word)

print(ans)