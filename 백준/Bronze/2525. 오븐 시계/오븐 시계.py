A, B = map(int, input().split())
C = int(input())

H = A
M = B + C

if M < 60:
    print(H, M)
else:
    H = A + (B + C)//60
    M = (B + C)%60
    if H >= 24:
        H = H % 24
    print(H, M)