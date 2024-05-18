from collections import Counter


def make_palindrome(string):
    counter = Counter(string)
    odd_count = 0
    odd_char = ""
    half_palindrome = ""

    # 홀수 개수인 문자의 개수 확인
    for char, cnt in sorted(counter.items()):
        if cnt % 2 == 1:
            odd_count += 1
            odd_char = char
        half_palindrome += char * (cnt//2)

        if odd_count > 1:
            return "I'm Sorry Hansoo"

    if odd_count == 1:
        full_palindrome = half_palindrome + odd_char + half_palindrome[::-1]
    else:
        full_palindrome = half_palindrome + half_palindrome[::-1]
    return full_palindrome


name = input()
palindrome = make_palindrome(name)
print(palindrome)