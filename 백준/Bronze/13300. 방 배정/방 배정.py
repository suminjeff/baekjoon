# 총 학생 수 N, 한 방 제한인원 K
N, K = map(int, input().split())

# 0 = 여, 1 = 남
# 성별, 학년
arr = [list(map(int, input().split())) for _ in range(N)]

girls = []
boys = []
for i in range(N):
    gender, year = arr[i][0], arr[i][1]
    if gender == 0:
        girls.append(year)
    else:
        boys.append(year)
girls.sort()
boys.sort()

stack0 = []
room0 = 0
top0 = -1

stack1 = []
room1 = 0
top1 = -1
for j in range(len(girls)):
    year0 = girls[j]
    if not stack0:
        stack0.append(year0)
        room0 += 1
        top0 += 1
    else:
        if stack0[top0] != year0:
            stack0.clear()
            stack0.append(year0)
            room0 += 1
            top0 = 0
        elif len(stack0) == K:
            stack0.clear()
            stack0.append(year0)
            room0 += 1
            top = 0
        else:
            stack0.append(year0)
            top0 += 1

for k in range(len(boys)):
    year1 = boys[k]
    if not stack1:
        stack1.append(year1)
        room1 += 1
        top1 += 1
    else:
        if stack1[top1] != year1:
            stack1.clear()
            stack1.append(year1)
            room1 += 1
            top1 = 0
        elif len(stack1) == K:
            stack1.clear()
            stack1.append(year1)
            room1 += 1
            top1 = 0
        else:
            stack1.append(year1)
            top1 += 1

ans = room0 + room1
print(ans)