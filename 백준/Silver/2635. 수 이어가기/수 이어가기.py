def fibonacci(N, i):
    if N - i < 0:
        stack.append(N)
        stack.append(i)
        return
    else:
        stack.append(N)
        fibonacci(i, N-i)


T = 1
for tc in range(1, T+1):
    N = int(input())
    max_len = 0
    ans = []
    for i in range(1, N+1):
        stack = []
        fibonacci(N, i)
        if max_len < len(stack):
            max_len = len(stack)
            ans = stack
    print(len(ans))
    print(*ans)