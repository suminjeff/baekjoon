word = input()
alphabet = [chr(_) for _ in range(97, 123)]

for letter in alphabet:
    if letter in word:
        print(word.index(letter), end=" ")
    else:
        print(-1, end=" ")