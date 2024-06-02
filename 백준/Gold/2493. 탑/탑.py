def find_receivers(tower_heights):
    n = len(tower_heights)
    result = [0] * n
    stack = []

    for i in range(n):
        while stack and tower_heights[stack[-1]] <= tower_heights[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1] + 1
        else:
            result[i] = 0
        stack.append(i)

    return result

# 입력 받기
n = int(input())
tower_heights = list(map(int, input().split()))

# 결과 계산
result = find_receivers(tower_heights)

# 결과 출력
print(' '.join(map(str, result)))
