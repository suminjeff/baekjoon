import sys

# 17071

LIMIT = 500_000

if __name__ == '__main__':
    N, K = map(int, input().split())

    visited = [[-1, -1] for _ in range(LIMIT + 1)]

    if N == K:
        print(0)
        exit()

    que = [N]
    time = 1
    K += time

    while True:
        if K > LIMIT:
            break

        next_que = []

        for subin in que:
            for next_subin in [subin + 1, subin - 1, subin * 2]:
                if 0 <= next_subin <= LIMIT and visited[next_subin][time % 2] == -1:
                    next_que.append(next_subin)
                    visited[next_subin][time % 2] = time

        if visited[K][time % 2] != -1:
            print(time)
            exit()

        time += 1
        K += time
        que = next_que

    print(-1)