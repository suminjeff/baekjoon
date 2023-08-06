T = int(input())

for _ in range(1, T+1):
    tc = int(input())
    arr = list(map(int, input().split()))
    counts = [0] * (max(arr)+1)
    for score in arr:
        counts[score] += 1

    max_idx = 0
    for i in range(len(counts)):
        if counts[max_idx] <= counts[i]:
            max_idx = i

    print(f"#{tc} {max_idx}")
