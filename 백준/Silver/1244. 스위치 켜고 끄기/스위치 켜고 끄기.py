def SWITCH(i):
    global arr
    if arr[i] == 0:
        arr[i] = 1
    else:
        arr[i] = 0


arr_len = int(input())
arr = list(map(int, input().split()))
n = int(input())
for _ in range(n):
    gen, switch = map(int, input().split())
    for i in range(arr_len):
        if gen == 1 and (i + 1) % switch == 0:
            SWITCH(i)
        elif gen == 2 and i == switch - 1:
            SWITCH(i)
            left = i - 1
            right = i + 1
            while True:
                if 0 <= left < arr_len and 0 <= right < arr_len:
                    if arr[left] == arr[right]:
                        SWITCH(left)
                        SWITCH(right)
                        left -= 1
                        right += 1
                    else:
                        break
                else:
                    break

for i in range(arr_len):
    print(arr[i], end=" ")
    if i % 20 == 19:
        print()
