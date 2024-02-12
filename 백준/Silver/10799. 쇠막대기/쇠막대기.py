import sys
input = sys.stdin.readline
# 10799

pipe = input().rstrip()
N = len(pipe)
stack = []
M = 0
for i in range(N):
    p = pipe[i]
    if p == "(":
        stack.append(p)
    elif p == ")":
        if pipe[i-1] == "(":
            stack.pop()
            M += len(stack)
        else:
            stack.pop()
            M += 1
print(M)