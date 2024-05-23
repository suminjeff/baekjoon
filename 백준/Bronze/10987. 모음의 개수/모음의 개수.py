# 10987

word = input()
ans = len(list(filter(lambda x: x in ['a', 'e', 'i', 'o', 'u'], word)))
print(ans)