N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

# 최소 공유기 거리
start = 1

# 최대 공유기 거리
end = houses[-1] - houses[0]

ans = 0

while start <= end:
    # mid: 현재 공유기 거리
    mid = (start + end) // 2
    current = houses[0]
    cnt = 1

    # 공유기 설치를 몇 개 할 수 있는지 확인
    for i in range(1, len(houses)):
        if houses[i] >= current + mid:
            cnt += 1
            current = houses[i]

    # 공유기 설치 수가 C보다 크면 공유기 사이의 거리를 늘림
    if cnt >= C:
        start = mid + 1
        ans = mid

    # 공유기 설치 수가 C보다 작으면 공유기 사이의 거리를 줄임
    else:
        end = mid - 1

print(ans)