import sys
input = sys.stdin.readline


def pick(n, depth, points, picked):
    global min_sum
    if points >= min_sum:
        return
    if depth == n:
        min_sum = min(min_sum, points)
        return
    for i in range(6):
        if used[i] == 0:
            flag = True
            for j in picked:
                if i + j == 5:
                    flag = False
            if flag:
                used[i] = 1
                picked.append(i)
                pick(n, depth+1, points+dice[i], picked)
                picked.pop()
                used[i] = 0

inf = int(1e9)
N = int(input())
dice = list(map(int, input().split()))
ans = 0
min_sum = inf
used = [0]*6
if N < 3:
    # N = 1일 때) 최대값만 빼주기
    # N = 2일 때) 면 3개가 보이는 곳 = 위 코너 (항상 4개), 면 2개가 보이는 곳 아래 코너 (항상 4개)
    if N == 1:
        ans += sum(dice) - max(dice)
    elif N == 2:
        # 3개 조합 (abc, abd, ace, ade, fbc, fbd, fcd, fde)
        pick(3, 0, 0, [])
        ans += min_sum * 4

        min_sum = inf

        pick(2, 0, 0, [])
        ans += min_sum * 4

else:
    # 면 3개가 보이는 곳 = 위 코너 (항상 4개)
    pick(3, 0, 0, [])
    ans += min_sum * 4
    min_sum = inf
    # 면 2개가 보이는 곳 = 맨위(N-2)*4 + 기둥(N-1)*4
    pick(2, 0, 0, [])
    ans += min_sum * ((N-2)*4 + (N-1)*4)
    # 면 1개만 보이는 곳 = ((N-2)*(N-1)*4 + (N-2)**2)
    ans += min(dice) * ((N-2)*(N-1)*4 + (N-2)**2)
print(ans)
