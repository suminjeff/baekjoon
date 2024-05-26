dictionary = {chr(x):0 for x in range(97, 97+26)}

word1 = input()
for letter in word1:
    dictionary[letter] += 1

word2 = input()
for letter in word2:
    dictionary[letter] -= 1

ans = 0
for i in dictionary.keys():
    ans += abs(dictionary[i])

print(ans)