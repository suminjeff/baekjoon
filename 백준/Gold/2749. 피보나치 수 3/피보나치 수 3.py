n = int(input())

M = 10**6
P = 15 * (10**5)

if n == 1:
    print("1")
else:
    arr = [0, 1]
    for j in range(2, n % P + 1):
        arr.append((arr[j - 1] + arr[j - 2]) % M)
    print(arr[n % P])