from collections import deque

def solve(n):
    que = deque([_ for _ in range(1, n+1)])
    while len(que) > 1:
        print(que.popleft(), end=" ")
        que.append(que.popleft())
    print(que.popleft())



if __name__ == '__main__':
    N = int(input())
    solve(N)
