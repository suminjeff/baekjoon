T = 1
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    stack1 = []
    top1 = -1
    ans1 = 0

    stack2 = []
    top2 = -1
    ans2 = 0
    for i in range(N):
        if stack1:
            if arr[i] >= stack1[top1]:
                stack1.append(arr[i])
                top1 += 1
            else:
                stack1.clear()
                stack1.append(arr[i])
                top1 = 0
        else:
            stack1.append(arr[i])
            top1 += 1
        if ans1 < len(stack1):
            ans1 = len(stack1)

        if stack2:
            if arr[i] <= stack2[top2]:
                stack2.append(arr[i])
                top2 += 1
            else:
                stack2.clear()
                stack2.append(arr[i])
                top2 = 0
        else:
            stack2.append(arr[i])
            top2 += 1
        if ans2 < len(stack2):
            ans2 = len(stack2)

    ans = max(ans1, ans2)
    print(ans)