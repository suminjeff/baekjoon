# 2457

N = int(input())

flowers = []
for _ in range(N):
    sm, sd, em, ed = map(int, input().split())
    sm, em = sm * 100, em * 100
    flowers.append([sm+sd, em+ed])
flowers.sort(key=lambda x: (x[0], x[1]))

answer = 0
end_date = 0
start_date = 301

while flowers:
    if start_date > 1130 or start_date < flowers[0][0]:
        break

    for _ in range(len(flowers)):
        if start_date >= flowers[0][0]:
            if end_date <= flowers[0][1]:
                end_date = flowers[0][1]
            flowers.remove(flowers[0])
        else:
            break
    start_date = end_date
    answer += 1

if start_date <= 1130:
    print(0)
else:
    print(answer)
