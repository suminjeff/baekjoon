import sys
input = sys.stdin.readline

string = input().rstrip()
bomb = input().rstrip()

N, M = len(string), len(bomb)

stack = []

for i in range(N):
    stack.append(string[i])
    if ''.join(stack[-M:]) == bomb:
        for _ in range(M):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')