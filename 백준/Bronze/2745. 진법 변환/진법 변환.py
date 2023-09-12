N, B = input().split()
B = int(B)

ans = 0
for i in range(len(N)):
    if B > 10:
        if N[len(N)-1-i].isnumeric():
            ans += B ** i * int(N[len(N) - 1 - i])
        else:
            ans += B**i * (ord(N[len(N)-1-i]) - 55)
    else:
        ans += B**i * int(N[len(N)-1-i])
print(ans)