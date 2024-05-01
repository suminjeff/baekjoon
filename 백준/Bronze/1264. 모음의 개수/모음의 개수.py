vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    S = input()
    if S == '#':
        break
    cnt = 0
    for s in S:
        if s in vowels:
            cnt += 1
    print(cnt)