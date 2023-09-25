arr = list(map(int, input().split()))
res = 0
for n in arr:
    res += n**2
print(res%10)

