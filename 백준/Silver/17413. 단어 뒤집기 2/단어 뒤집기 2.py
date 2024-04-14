import sys

S = input()
stack = []
ans = ''
check = False

for s in S:
    if s == '<':
        check = True
        for _ in range(len(stack)):
            ans += stack.pop()
    stack.append(s)

    if s == '>':
        check = False
        for _ in range(len(stack)):
            ans += stack.pop(0)

    if s == ' ' and check == False:
        for i in range(len(stack)):
            if i == 0:
                stack.pop()
                continue
            ans += stack.pop()
        ans += ' '

if stack:
    for _ in range(len(stack)):
        ans += stack.pop()
print(ans)