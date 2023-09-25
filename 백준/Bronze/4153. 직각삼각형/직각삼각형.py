while True:
    arr = list(map(int, input().split()))
    if arr == [0, 0, 0]:
        break
    max_v = arr.pop(arr.index(max(arr)))
    if max_v ** 2 == arr[0] ** 2 + arr[1] ** 2:
        print("right")
    else:
        print("wrong")