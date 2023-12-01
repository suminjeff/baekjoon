word = input().rstrip()
for w in word:
    if w.isupper():
        print(w.lower(), end='')
    else:
        print(w.upper(), end='')
