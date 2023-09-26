word = input().upper()
wordset = set(word)
max_letter = ""
max_cnt = 0
for letter in wordset:
    cnt = word.count(letter)
    if max_cnt == cnt:
        max_letter = "?"
    elif max_cnt < cnt:
        max_cnt = cnt
        max_letter = letter
print(max_letter)