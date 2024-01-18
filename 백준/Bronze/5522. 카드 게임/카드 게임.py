ans = 0
while True:
    try:
        x = int(input())
        ans += x
    except:
        break
print(ans)