import sys
import copy
input = sys.stdin.readline


def cnt(temp_list):
    global X
    res = 0
    for i in range(N):
        flag = True
        clone = copy.deepcopy(temp_list[i])
        for j in range(len(temp_list[i]) - 1):
            block1, block2 = temp_list[i][j], temp_list[i][j+1]
            clone1, clone2 = clone[j], clone[j+1]
            v1, v2 = block1[0], block2[0]
            if v1 < v2:
                if v1 + 1 == v2:
                    if clone1.count(v1) < X:
                        flag = False
                        break
                    else:
                        x = 0
                        for k in range(len(block1)):
                            if clone1[k] != 0:
                                clone1[k] = 0
                                x += 1
                            if x == X:
                                break
                else:
                    flag = False
                    break
            elif v1 > v2:
                if v2 + 1 == v1:
                    if clone2.count(v2) < X:
                        flag = False
                        break
                    else:
                        x = 0
                        for k in range(len(block2)):
                            if clone2[k] != 0:
                                clone2[k] = 0
                                x += 1
                            if x == X:
                                break
                else:
                    flag = False
                    break
        if flag:
            res += 1
    return res


N, X = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
row_ans = 0
# 행 방향
row_blocks = []
for r in range(N):
    stack = []
    temp = []
    for c in range(N):
        v = arr[r][c]
        if stack:
            if v == stack[-1]:
                stack.append(v)
            else:
                temp.append(stack)
                stack = [v]
        else:
            stack.append(v)
        if c == N-1:
            temp.append(stack)
    row_blocks.append(temp)

# 열 방향
col_blocks = []
for c in range(N):
    stack = []
    temp = []
    for r in range(N):
        v = arr[r][c]
        if stack:
            if v == stack[-1]:
                stack.append(v)
            else:
                temp.append(stack)
                stack = [v]
        else:
            stack.append(v)
        if r == N-1:
            temp.append(stack)
    col_blocks.append(temp)

ans += cnt(row_blocks)
ans += cnt(col_blocks)
print(ans)